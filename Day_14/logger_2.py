'''Program to explore logging module in python'''
import logging
import requests
import logger
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("logger.log")
formatter=logging.Formatter("%(asctime)s:%(name)s:%(message)s:%(levelname)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# logging.basicConfig(filename="logger.log", level=logging.DEBUG,
#                     format="%(filename)s:%(levelname)s:%(message)s")
try:
    r=requests.get("http://httpbin.org/basic-auth/user/pass", auth=("user","pass"))
    logger.info(r.url)
except Exception as e:
    logger.error(e)
