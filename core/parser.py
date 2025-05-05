from playwright.async_api import async_playwright
from config.settings import settings
from config.logger_config import logger

async def parse_trains():
    """ Parce trains from RW.BY """
    logger.info("Starting parsing trains")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            logger.info("chromium starting")
            await page.goto(settings.RWBY_URL, timeout=settings.RWBY_TIMEOUT)

            logger.info("wait for page to load")
            await page.wait_for_load_state("networkidle")

            logger.info("wait for selector to load")
            await page.wait_for_selector(".sch-table__row", timeout=100000)

            trains = []
            all_rows = await page.query_selector_all(".sch-table__row")

            logger.info("trains loading")
            for row in all_rows[1:]:
                btn_wrap = await row.query_selector(".sch-table__btn-wrap")
                train_route = await row.query_selector(".train-route")
                train_route_text = await train_route.inner_text() if train_route else None

                train_from_time = await row.query_selector(".train-from-time")
                train_from_time_text = await train_from_time.inner_text() if train_from_time else None

                train = {
                    "has_tickets": await btn_wrap.is_visible() if btn_wrap else False,
                    "train_route": train_route_text.replace('\xa0', ' '),
                    "train_from_time": train_from_time_text,
                }
                trains.append(train)

            return trains
        except Exception as e:
            logger.error(e)

        finally:
            await browser.close()