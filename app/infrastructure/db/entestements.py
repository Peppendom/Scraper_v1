from app.infrastructure.db.setup import create_session, init_db
from app.infrastructure.db.repositories import CarRepository
# from app.infrastructure.scrapers import main as scrap
# from app.application.parsers import CarParser
import asyncio


# async def entestements_saving_to_db():
#     async with await create_session() as session:
#         # session = await create_session()
#         car_repo = CarRepository(session = session)
#         html = await scrap()
#         parser = CarParser()
#         car = parser.parse_all_data(html = )
#         await car_repo.add_car(car)
#         # await session.close()
#         return car


async def entestements_retrieving_from_db():
    async with await create_session() as session:
        car_repo = CarRepository(session = session)
        a_car = await car_repo.get_car_by_url(url = "https://auto.ria.com/uk/auto_land_rover_range_rover_velar_38325532.html")
        return a_car


async def entestements_retrieve_all():
    async with await create_session() as session:
        car_repo = CarRepository(session = session)
        all_cars = await car_repo.get_all_cars()
        return all_cars


async def entestements_filtration():
    async with await create_session() as session:
        car_repo = CarRepository(session=session)
        new_list = await car_repo.filter_existing_urls(["https://auto.ria.com/uk/auto_land_rover_range_rover_velar_38325532.html",
                                              "Some new unexisting url",
                                                        "and another one"])
        return new_list


async def entestements_delete():
    async with await create_session() as session:
        car_repo = CarRepository(session=session)
        await car_repo.delete_all()


async def main():
    await init_db()

    await entestements_delete()


    # carito = await entestements_retrieve_all()
    # print(carito)
    # print(type(carito))
    # for car in carito:
    #     # print(car.title)
    #     print(car.url)


if __name__ == "__main__":
    asyncio.run(main())