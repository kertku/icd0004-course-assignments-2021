from framework.booking_api import BookingApi
from framework.request.booking import Booking

if __name__ == '__main__':
    booking_api = BookingApi()
    print(booking_api.post_booking(Booking().get_fully_payload().toJSON()).content)
