import datetime
import json
from dataclasses import dataclass

from faker import Faker

from framework.request.booking_dates import BookingDates


@dataclass
class Booking:
    firstname: str = " "
    lastname: str = " "
    totalprice: float = 1
    depositpaid: bool = True
    bookingdates: BookingDates = BookingDates(datetime.date.today(), datetime.date.today())
    additionalneeds: str = ""

    def __getitem__(self, item):
        return getattr(self, item)

    def get_fully_payload(self):
        faker = Faker("et_EE")
        fake_additional_needs = ["sauna", "rätikut", "äratust", "seda mida on pakkuda"]
        self.bookingdates = BookingDates(faker.date_this_year(), faker.unique.date_this_year())
        self.firstname = faker.first_name()
        self.lastname = faker.last_name()
        self.totalprice = faker.random.randint(50, 280)
        self.depositpaid = True
        self.additionalneeds = f"Vajan {faker.words(1, fake_additional_needs, True)[0]}!"
        return self

    @staticmethod
    def JSON_converter(o):
        if isinstance(o, datetime.date):
            return o.__str__()
        return o.__dict__

    def toJSON(self):
        return json.dumps(self, default=self.JSON_converter, indent=4)


