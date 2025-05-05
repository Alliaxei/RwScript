import asyncio
from core.parser import parse_trains
from core.telegram_notifier import send_message
from config.logger_config import logger

async def main():
    logger.info(f"Parsing trains from RW.BY ...")
    trains = await parse_trains()
    if not trains:
        logger.info(f"No trains found, exiting...")
        return

    for train in trains:
        print(train)
    await send_message(trains)


if __name__ == "__main__":
    asyncio.run(main())