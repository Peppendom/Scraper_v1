# Standard libraries
import asyncio
import os

# Third-party libraries
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv
from playwright.async_api import async_playwright

# Modules
from app.infrastructure import db, crawlers, scrapers
from app.application import parsers, use_cases
from app.config import (
    CRON_SLEEPING_TIME,
    DUMP_CRON_SCHEDULE as DUMP_TIME,
    SCRAPING_CRON_SCHEDULE as SCRAPING_TIME
)
from app.utils import log


log(msg = "Scraper started", level = "INFO")
load_dotenv()

async def start_scraper():
    base_url = os.getenv("BASE_SCRAPING_URL")

    await db.setup.init_db()
    session = await db.setup.create_session()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = True)
        crawler = crawlers.CarCrawler(browser = browser, base_url = base_url)
        scraper = scrapers.CarScraper(browser = browser)
        parser = parsers.CarParser()
        repo = db.repositories.CarRepository(session = session)
        use_case = use_cases.ScrapingUseCase(
            scraper = scraper,
            crawler = crawler,
            parser = parser,
            repo = repo
        )

        await use_case.run()
        await session.close()
        await browser.close()


def start_cronjobs():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        start_scraper,
        CronTrigger(**SCRAPING_TIME)
    )

    scheduler.add_job(
        db.utils.dump_db,
        CronTrigger(**DUMP_TIME)
    )

    scheduler.start()


async def main():
    start_cronjobs()
    log(msg = "Cronjobs activated", level = "INFO")
    while True:
        await asyncio.sleep(CRON_SLEEPING_TIME)


if __name__ == "__main__":
    asyncio.run(main())
