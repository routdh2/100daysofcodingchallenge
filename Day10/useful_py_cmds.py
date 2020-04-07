'''Useful python commands we should know'''
if __name__=="__main__":
    '''1. Ternary Operators in python'''
    raining=True
    # if raining:
    #     go_out=0
    # else:
    #     go_out=1
    # print(go_out)
    go_out=0 if raining else 1 #one-liner ternary operator
    print(go_out)

    '''2. Underscore placeholders for large nums for readability'''
    num1=10_000_000_000_000 #placing _ doesn't affect the num
    num2=349_933_339_994
    print(num1) #prints 10000000000000
    '''To format string use f string'''
    print(f"{num1:,}") #prints 10,000,000,000,000
    '''it only takes comma(,) as the formatting option for int. other chars will result in error'''

    '''3. Context Managers can be useful while handling system resources
    like files, thread locks, DB connections etc.'''
    # with open("sample.txt","r") as rf:
    #     print(rf.readlines())

    '''4. Use enumerators to loop through index and value together'''
    nums=[1,2,3,4]
    for index,value in enumerate(nums):
        print(index, end=" ") #print 0 1 2 3
    for item in enumerate(nums):
        print(item, end=" ") # prints (0, 1) (1, 2) (2, 3) (3, 4)
    '''So enumerate returns a tuple object and we unpack it using vars'''
    for item in enumerate(nums,start=1):
        print(item,end="") #prints (1, 1)(2, 2)(3, 3)(4, 4)
    for index,_ in enumerate(nums): #if you don't want to use value, use _ in place of that
        print(index,end=" ")
    print()

    '''5. zip is used to loop through two or more iterables at the same time'''
    list1=[1,2,3,4]
    list2=["apples","oranges","mangoes","pineapples","peaches"]
    for i,j in zip(list1,list2):
        print(i,"->",j, end=" ") #prints 1 -> apples 2 -> oranges 3 -> mangoes 4 -> pineapples
    '''zip returns a tuple and it loops through the shortest of all iterables
    in this ex: peaches is not printed'''
    #zip can be used for mulitple lists
