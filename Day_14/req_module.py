'''Program to explore the "requests" module in Python'''
if __name__=="__main__":
    import requests
    url="https://httpbin.org/get"
    payload={"name":"Dhananjay","age":26}
    r=requests.get(url,params=payload) #prepares the url with the params and makes a connection
    with open("web_img.jpg","wb") as wf:
        wf.write(r.content) #you can copy the content of the response to a file
    print(r.status_code)
    print(r.ok) #returns True if HTTP status code is below 400
    print(r.headers)
    print(r.text) #returns response in String format

    '''HTTP post methods'''
    url="https://httpbin.org/post"
    payload={"name":"Dhananjay", "age":23}
    r=requests.post(url, data=payload) #makes a HTTP post connection with the payload
    print(r.status_code)
    print(r.ok)
    text=r.text
    print(text, type(text)) #r.text() returns object of type str
    print(r.headers)
    json_ob = r.json() #converts the response to JSON object
    print(json_ob, type(json_ob)) #r.json() returns object of type dict

    print(json_ob['form']['age'])

    '''HTTP authentication'''
    username="user"
    password="pass"
    url=f"https://httpbin.org/basic-auth/{username}/{password}"
    r=requests.get(url, auth=("user","pass")) #makes a connection with authentication values
    print(r.ok)
    print(r.text)
    print(r.status_code)

    '''Setting timeout for HTTP requests'''
    delay=3
    url=f"http://httpbin.org/delay/{delay}"
    r=requests.get(url, timeout=2) #timeout is in seconds, The req gets timeout after the specified seconds
    print(r)
    print(r.ok)
    print(r.text)
