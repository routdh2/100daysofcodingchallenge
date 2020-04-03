#program to understand the concept of generators in python
if __name__=="__main__":
    nums=[1,2,3,4,5]
    square_list=[]
    for i in nums:
        square_list.append(i**2)
    print(square_list)
    def generate_squares(nums):
        for i in nums:
            yield i ** 2
    list_gen=generate_squares(nums) #this is a generator object
    # print(list(list_gen))
    for item in list_gen:
        print(item)
    list_gen2=(i*i for i in nums) #this is also a generator object
    # print(list_gen2)
    print(next(list_gen2))
    for item in list_gen2:
        print(item,end=' ')
