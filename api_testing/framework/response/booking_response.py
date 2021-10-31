from dataclasses import dataclass
from framework.request.booking import Booking


@dataclass
class BookingResponse:
    bookingid: int
    booking: Booking
