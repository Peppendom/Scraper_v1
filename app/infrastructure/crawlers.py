from playwright.async_api import Browser, Page
from app.config import MAX_LINKS_LIMIT as LIMIT


class CarCrawler:
    def __init__(self, browser: Browser, base_url: str):
        self.browser = browser
        self.base_url = base_url

    async def get_one_page_car_links(self, page_url: str) -> list[str]:
        page: Page = await self.browser.new_page()
        await page.goto(page_url)
        links = await page.eval_on_selector_all(
            "a.m-link-ticket",
            "elements => elements.map(el => el.href)"
        )
        await page.close()
        return links


    async def get_car_links_batch(self, limit = LIMIT):
        total = 0
        page_number = 1
        while True:
            if limit is not None and total >= limit:
                break

            url = self.base_url if page_number == 1 else f"{self.base_url}?page={page_number}"

            car_links = await self.get_one_page_car_links(url)

            if not car_links:
                break

            if limit:
                remaining = limit - total
                car_links = car_links[:remaining]

            yield car_links

            total += len(car_links)
            page_number +=1
