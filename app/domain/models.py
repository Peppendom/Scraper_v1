from dataclasses import dataclass
from datetime import datetime


@dataclass
class Car:
    url: str
    title: str | None
    price_usd: int | None
    odometer: int | None
    username: str | None
    phone_number: int | None
    image_url: str | None
    images_count: int | None
    car_number: str | None
    car_vin: str | None
    datetime_found: datetime
