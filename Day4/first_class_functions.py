#Understanding first class functions in python
'''We should be able to treat the function just like any
other variable/object'''
if __name__=="__main__":
    def square_root(num):
        return num**0.5
    '''function getting called and value is returned'''
    val=square_root(5)
    '''val is a variable of type float'''
    print(val,type(val))
    # 2.23606797749979 <class 'float'>
    '''function getting assigned to a variable just like any other variable/object'''
    val=square_root
    '''val is now a function referring to square_root function'''
    print(val,type(val))
    # <function square_root at 0x00AAC6E8> <class 'function'>
    print(val(5))


