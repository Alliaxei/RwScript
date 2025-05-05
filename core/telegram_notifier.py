import aiohttp

from config.logger_config import logger
from config.settings import settings

async def send_message(trains_data) -> bool:
    if not settings.TELEGRAM_TOKEN:
        logger.error("Telegram token not set")
        return False

    if not settings.TELEGRAM_CHAT_ID:
        logger.error("Telegram chat id not set")
        return False
    formatted_message = format_trains_markdown(trains_data)

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "text": formatted_message,
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "parse_mode": "MarkdownV2"
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(error_text)
                    return False
                return True
    except Exception as e:
        logger.error(e)
        return False


def escape_markdown(text: str) -> str:
    if not text:
        return ""
    escape_chars = '_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{char}' if char in escape_chars else char for char in text)


def format_trains_markdown(trains_data: list) -> str:
    """
    :param trains_data: Список словарей с данными о поездах
    :return: Отформатированная строка
    """
    if not trains_data:
        return escape_markdown("🚂 Расписание поездов\n\nПоездов не найдено")

    message = [
        "*🚂 Расписание поездов*",
        f"*Найдено поездов:* {len(trains_data)}",
        "",
        "*Маршруты:*",
    ]

    for i, train in enumerate(trains_data, 1):
        has_tickets = "✅ Доступны" if train.get('has_tickets') else "❌ Нет билетов"
        route = escape_markdown(train.get('train_route', 'Н/Д'))
        time = escape_markdown(train.get('train_from_time', 'Н/Д'))

        message.append(
            f"{i}\\. *{route}*\n"
            f"   *Время:* `{time}` \\| {has_tickets}"
        )

    return "\n".join(message)
