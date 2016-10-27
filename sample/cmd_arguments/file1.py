import colorlog
import begin


def main():

    logger = colorlog.getLogger()
    logger.setLevel(colorlog.colorlog.logging.DEBUG)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    logger.debug("Debug message")
    logger.info("Information message")
    logger.error("Error message")
    logger.critical("Critical message")
