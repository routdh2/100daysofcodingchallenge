'''functions can be passed as an argument to another function.
Those functions are called higher order functions'''
if __name__=="__main__":
    '''my_map is a higher order function which takes function as arguments'''
    def my_map(func,nums):
        result=[]
        for item in nums:
            result.append(func(item))
        return result
    def square_root(num):
        return num**0.5
    nums=[1,2,3,4,5]
    '''we are passing square_root function as a parameter to my_map function'''
    result=my_map(square_root,nums)
    print(result)
