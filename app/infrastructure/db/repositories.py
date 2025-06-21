from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.models import Car as CarDB
from app.domain.models import Car as CarDomain
from app.utils import log


class CarRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_car(self, car: CarDomain) -> None:
        car_db = CarDB(
            url = car.url,
            title = car.title,
            price_usd = car.price_usd,
            odometer = car.odometer,
            username = car.username,
            phone_number = car.phone_number,
            image_url = car.image_url,
            images_count = car.images_count,
            car_number = car.car_number,
            car_vin = car.car_vin,
            datetime_found = car.datetime_found
        )

        self.session.add(car_db)
        await self.session.commit()


    async def add_list_of_cars(self, list_of_cars: list[CarDomain]) -> None:
        mapped_list = []
        for car in list_of_cars:
            car_db = CarDB(
                url=car.url,
                title=car.title,
                price_usd=car.price_usd,
                odometer=car.odometer,
                username=car.username,
                phone_number=car.phone_number,
                image_url=car.image_url,
                images_count=car.images_count,
                car_number=car.car_number,
                car_vin=car.car_vin,
                datetime_found=car.datetime_found
            )
            mapped_list.append(car_db)

        self.session.add_all(mapped_list)
        await self.session.commit()


    async def delete_all(self) -> None:
        await self.session.execute(delete(CarDB))
        await self.session.commit()
        log("All cars were deleted from database")


    async def filter_existing_urls(self, list_of_urls: list[str]) -> list[str]:
        statement = select(CarDB.url).where(CarDB.url.in_(list_of_urls))
        result = await self.session.execute(statement)
        existing_urls = {row[0] for row in result.fetchall()}
        return [url for url in list_of_urls if url not in existing_urls]


    async def get_all_cars(self) -> list[CarDB]:
        stmt = select(CarDB)
        result = await self.session.execute(stmt)
        return result.scalars().all()


    async def get_car_by_url(self, url: str) -> CarDB:
        stmt = select(CarDB).where(CarDB.url == url)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
