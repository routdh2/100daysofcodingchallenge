'''Program to understand iterators and iterables in python'''
if __name__=="__main__":
    list1=[1,2,3] #list is iterable but not an iterator
    for i in list1:
        print(i)
    print(dir(list1)) #it has __iter__() method but no __next__() method
    num_iterator=list1.__iter__() #we call __iter__() method to get an iterator on our object
    print(num_iterator) #it's an iterator object
    i_num=iter(list1) #we can call like this as well to get an iterator object
    print(i_num)
    print(dir(i_num)) #it has __iter__() method as well as __next__() method
    #an iterator object is both iterable and also acts as an iterator
    # for i in i_num:
    #     print(i)
    print(next(num_iterator)) #next() returns the next value in the iterator object
    print(next(i_num)) #next() method calls __next__() method in iterator
    print(next(num_iterator))
    print(next(i_num)) #after the iterator object gets exhausted, it raises StopIteration error

    '''So basically, an object is iterable if it has __iter__() method which returns an iterator
    While an iterator is an object which has both __next__() method and __iter__() method'''
    while True:
        try:
            print("inside while")
            print(next(num_iterator))
            print(next(i_num))
        except StopIteration:
            break
