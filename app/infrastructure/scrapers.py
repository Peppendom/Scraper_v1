from playwright.async_api import Browser, Page
from app.utils import log


class CarScraper:
    def __init__(self, browser: Browser):
        self.browser = browser

    async def fetch_html(self, url: str) -> str | None:
        try:
            page: Page = await self.browser.new_page()
            await page.goto(url)
            await page.click("a.phone_show_link")
            try:
                await page.wait_for_function(
                    'document.querySelector("span.phone.bold[data-phone-number]")?.getAttribute("data-phone-number") !== ""'
                )
            except:
                log(msg=f"Wasn't able to find phone number for page {url}", level="WARNING")
                pass
            container = await page.locator("body > div:nth-child(20) > div.ticket-status-0").element_handle()
            content = await container.inner_html() if container else ""
            await page.close()
            return content
        except:
            log(msg = f"Page {url} was not processed successfully", level = "WARNING")
