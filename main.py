import asyncio

from config.logger_config import logger
from core.parser import parse_trains
from core.telegram_notifier import send_message


async def main():
    logger.info("Parsing trains from RW.BY ...")
    trains = await parse_trains()

    logger.info("starting sending message to Telegram...")
    await send_message(trains)


if __name__ == "__main__":
    asyncio.run(main())
