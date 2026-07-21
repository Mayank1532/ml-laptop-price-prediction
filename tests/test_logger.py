from src.logger import logger


def test_logger():
    logger.info("=" * 60)
    logger.info("Starting Logger Module Test")

    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")

    logger.info("Logger Module Test Completed Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    test_logger()
