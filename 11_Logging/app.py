import logging
## logging settings 
logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s -%(message)s',
    datefmt= '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app2.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('Airthmethic_App')
def add(a,b):
    result = a+b
    logger.info(f"Adding {a} + {b}")
    return result

def Subtract(a,b):
    result = a-b
    logger.info(f"Subtract {a} - {b}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error.")
        return None
add(10,20)
Subtract(15,10)
divide(10,2)
