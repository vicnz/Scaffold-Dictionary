import logging
logger_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename='error.log',
    filemode='w+',
    format=logger_format,
    level=logging.ERROR,
)

logger = logging.getLogger()

# logger.error("Logged Error")