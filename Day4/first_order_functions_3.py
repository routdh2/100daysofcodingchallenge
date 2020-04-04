'''functions can be returned from a function'''
if __name__=="__main__":
    def logger(message):
        def greeting(name):
            return message+" "+name
        return greeting
    '''func is a function which is being returned by logger'''
    func=logger("Hello")
    '''<function logger.<locals>.greeting at 0x0384C730> <class 'function'>'''
    print(func,type(func))
    print(logger) #<function logger at 0x02D3C778>
    print(func("Dhananjay")) # Hello Dhananjay
    print(func("Tanmay"))
    func_2=logger("Hi")
    print(logger) #<function logger at 0x02D3C778>
    '''<function logger.<locals>.greeting at 0x0384C6E8>
    Each time you call logger function it creates a new function object
    you can see by analyzing their memory locations'''
    print(func_2)
    print(func_2("Everyone!"))
    #greeting("Error") -- results in NameError: name 'greeting' is not defined
