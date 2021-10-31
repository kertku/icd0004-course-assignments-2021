import datetime
from dataclasses import dataclass


@dataclass()
class BookingDates:
    checkin: datetime.date
    checkout: datetime.date
