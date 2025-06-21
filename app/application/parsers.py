# Standard libraries
from datetime import datetime

# Third-party libraries
from bs4 import BeautifulSoup

# Modules
from app.config import THOUSAND
from app.domain.models import Car


class CarParser:
    def __init__(self):
        pass


    def parse_all_data(self, html: str, url: str) -> Car:
        soup = BeautifulSoup(html, features="html.parser")
        url = url

        return Car(
            url = url,
            title = self._parse_title(soup),
            price_usd = self._parse_price(soup),
            odometer = self._parse_odometer(soup),
            username = self._parse_username(soup),
            phone_number = self._parse_phone_number(soup),
            image_url = self._parse_image_url(soup),
            images_count = self._parse_images_count(soup),
            car_number = self._parse_license_plate(soup),
            car_vin = self._parse_car_vin(soup),
            datetime_found = self._get_time()
        )

    @staticmethod
    def _parse_title(soup: BeautifulSoup) -> str | None:
        tag = soup.find(name = "h1", class_ = "head")
        if not tag:
            return None
        return tag.get(key = "title")

    @staticmethod
    def _parse_price(soup: BeautifulSoup) -> int | None:
        tag = soup.find(name = "div", class_ = "price_value")
        if not tag:
            return None
        strong = tag.find("strong")
        if not strong:
            return None
        price_text = strong.text.replace(" ", "").replace("$", "")
        try:
            return int(price_text)
        except ValueError:
            return None

    @staticmethod
    def _parse_odometer(soup: BeautifulSoup) -> int | None:
        tag = soup.find(name = "span", class_ = "size18")
        if not tag:
            return None
        odometer_raw = tag.text.replace(" ","")
        try:
            return int(odometer_raw) * THOUSAND
        except ValueError:
            return None

    @staticmethod
    def _parse_username(soup: BeautifulSoup) -> str | None:
        tag = soup.find(name = "div", class_ = "seller_info_name bold")
        if not tag:
            return None
        return tag.text.replace(" ", "")

    @staticmethod
    def _parse_phone_number(soup: BeautifulSoup) -> int | None:
        tag = soup.find(name = "span", class_ = "phone bold")
        if not tag:
            return None
        raw_phone = tag.get(key = "data-phone-number", default = "")
        digits = str(''.join(d for d in raw_phone if d.isdigit()))
        if digits.startswith("38"):
            formatted_phone = digits
        else:
            formatted_phone = "38" + digits
        try:
            return int(formatted_phone)
        except ValueError:
            return None

    @staticmethod
    def _parse_image_url(soup: BeautifulSoup) -> str | None:
        tag = soup.find(name = "img", class_ = "outline m-auto")
        if not tag:
            return None
        return tag.get(key = "src") if tag else None

    @staticmethod
    def _parse_images_count(soup: BeautifulSoup) -> int | None:
        tag = soup.find(name = "a", class_ = "show-all link-dotted")
        if not tag:
            return None
        images_count_string = tag.text
        images_count = ''.join([c for c in images_count_string if c.isdigit()])
        try:
            return int(images_count)
        except ValueError:
            return None

    @staticmethod
    def _parse_license_plate(soup: BeautifulSoup) -> str | None:
        tag = soup.find(name = "span", class_ = "state-num ua")
        if not tag:
            return None
        return str(tag.contents[0]).replace(" ", "")

    @staticmethod
    def _parse_car_vin(soup: BeautifulSoup) -> str | None:
        tag = soup.find(name="span", class_="label-vin")
        if not tag:
            return None
        return str(tag.text).replace(" ", "")

    @staticmethod
    def _get_time() -> datetime:
        return datetime.now()
