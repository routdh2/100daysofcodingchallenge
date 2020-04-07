'''Program to find difference between == and is in python'''
if __name__=="__main__":
    list1=[1,2,3,4,5]
    list2=[1,2,3,4,5]
    print(True if list1==list2 else False) #prints True
    print(True if list1 is list2 else False) #prints False
    '''== checks for values in objects. 
    'is' checks for memory locations of the objects.'''
    print(id(list1)) #id() built-in method is used to find the memory loc of any object
    print(id(list2)) #turns out they are different
    list2=list1
    print(True if list1==list2 else False) #prints True since contents are equal
    print(True if list1 is list2 else False) #prints True since both objects refer to same mem loc
    print(id(list1))
    print(id(list2)) #both mem locs are same
