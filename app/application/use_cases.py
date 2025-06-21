from app.application.parsers import CarParser
from app.infrastructure.scrapers import CarScraper
from app.infrastructure.crawlers import CarCrawler
from app.infrastructure.db.repositories import CarRepository
from app.config import MAX_LINKS_LIMIT as LIMIT, SEMAPHORE_LIMITS
import asyncio
from app.utils import log


class ScrapingUseCase:
    def __init__(
            self,
            scraper: CarScraper,
            crawler: CarCrawler,
            parser: CarParser,
            repo: CarRepository,
    ):
        self.scraper = scraper
        self.crawler = crawler
        self.parser = parser
        self.repo = repo
        self.semaphore = asyncio.Semaphore(SEMAPHORE_LIMITS)


    async def limited_scrape(self, url: str):
        async with self.semaphore:
            return await self.scraper.fetch_html(url)

    async def run(self):
        async for batch in self.crawler.get_car_links_batch(limit = LIMIT):
            list_of_links_to_process = await self.repo.filter_existing_urls(batch)
            batch_html_results = await asyncio.gather(*(self.limited_scrape(url) for url in list_of_links_to_process))
            list_of_cars = []
            filtered_pairs = [(url, html) for url, html in zip(list_of_links_to_process, batch_html_results) if html]
            for url, html in filtered_pairs:
                car = self.parser.parse_all_data(html = html, url = url)
                list_of_cars.append(car)
            await self.repo.add_list_of_cars(list_of_cars)
            for car in list_of_cars:
                log(msg = f'{car.url} added to database.')
