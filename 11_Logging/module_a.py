import logging

def moudule_a_function():
    logger = logging.getLogger(__name__)
    logger.info("Module A function started")
    logger.debug("This is a message from module A")
    logger.info("Module A function finished")