import logging
# Configuring logging
logging.basicConfig(
    filename='app_1.log',
    filemode='w',
    level = logging.INFO,
    format='%(asctime)s%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  
)