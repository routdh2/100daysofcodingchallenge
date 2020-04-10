'''Program to explore the "logging" module in Python'''
'''
Logging Levels:
    Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
    Info : These are used to Confirm that things are working as expected
    Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
    Error : This tells that due to a more serious problem, the software has not been able to perform some function
    Critical : This tells serious error, indicating that the program itself may be unable to continue running
'''
if __name__=="__main__":
    import logging
    import requests
    logging.basicConfig(filename="requests.log", level=logging.DEBUG,
                        format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s")
    #invoke HTTP GET method
    url="http://httpbin.org/get"
    payload={"page":2,"count":23}
    r=requests.get(url,params=payload)
    logging.debug(f"Request URL: {r.url} Status Code: {r.status_code} Content: {r.json()}")

    #invoke HTTP POST method
    url="http://httpbin.org/post"
    payload={"name":"dhananjay","age":23}
    try:
        r=requests.post(url,data=payload)
        logging.debug(f"Request URL: {r.url} Status Code: {r.status_code} Content: {r.json()}")
    except Exception as e:
        logging.error(e)

    #invoke HTTP user authentication
    username="user"
    password="pass"
    url=f"http://httpbin.org/basic-auth/{username}/{password}"
    try:
        r=requests.get(url,auth=("user","pass"))
        logging.debug(f"Request URL: {r.url} Status Code: {r.status_code} Content: {r.json()}")
    except Exception as e:
        logging.error(e)

    #invoke HTTP timeout
    delay=4
    url=f"http://httpbin.org/delay/{delay}"
    try:
        r=requests.get(url,timeout=3)
        logging.debug(f"Request URL: {r.url} Status Code: {r.status_code} Content: {r.json()}")
    except Exception as e:
        logging.error(e)
