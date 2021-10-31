import requests


class BookingApi:
    base_url = "https://restful-booker.herokuapp.com"
    booking_api = base_url + "/booking/"

    def get_bookings(self):
        return requests.get(self.base_url)

    def get_booking_by_id(self, booking_id, content_type="application/json", accept="application/json"):
        return requests.get(self.booking_api + str(booking_id), {"content_type": content_type, "accept": accept})

    def post_booking(self, booking_payload, content_type="application/json", accept="application/json"):
        return requests.post(self.booking_api, data=booking_payload,
                             headers={"Content-Type": content_type, "Accept": accept})

    def put_booking(self, booking_id, auth_token, booking_payload, content_type="application/json",
                    accept="application/json"):
        return requests.put(f"{self.booking_api}{booking_id}", data=booking_payload,
                            headers={"Content-Type": content_type, "Accept": accept, "Cookie": f"token={auth_token}"})

    def delete_booking(self, booking_id, auth_token, content_type="application/json"):
        return requests.delete(f"{self.booking_api}{booking_id}",
                               headers={"Content-Type": content_type, "Cookie": f"token={auth_token}"})
