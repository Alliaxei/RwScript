import logging


def setup_logger():
    """ Creating logger """
    logger_set = logging.getLogger(__name__)
    logger_set.setLevel(logging.INFO)

    if logger_set.hasHandlers():
        logger_set.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)

    logger_set.addHandler(console_handler)
    logger_set.addHandler(file_handler)

    return logger_set

logger = setup_logger()