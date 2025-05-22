import logging

def moudule_b_function():
    logger = logging.getLogger(__name__)
    logger.info("Module B function started")
    logger.debug("This is a message from module B")
    logger.info("Module B function finished")