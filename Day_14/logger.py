'''Program to create your own logger for your module'''
import logging
import requests

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fileHandler=logging.FileHandler(filename="request.log")
fileHandler.setLevel(logging.ERROR)
formatter=logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)



# logging.basicConfig(filename="requests.log", level=logging.INFO,
#                     format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
url="http://httpbin.org/get"
try:
    r=requests.get(url)
    logger.info(r.url)
except Exception as e:
    logger.error(e)
