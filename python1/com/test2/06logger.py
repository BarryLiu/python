import logging

"""
logging log模块简单使用 
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('logging.log')
handler.setLevel(logging.INFO)

# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()
logger.addHandler(ch)


# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

logger.info('Hello baby')
logger.debug('A value for debugging')
logger.warning('A warning occurred (%d apples)', 42)
logger.error('An error occurred')

def info(msg):
	logger.info(msg)

def debug(msg):
	logger.debug(msg)

def warning(msg):
	logger.warning(msg)

def error(msg):
	logger.error(msg)


print('logger结束！！')



