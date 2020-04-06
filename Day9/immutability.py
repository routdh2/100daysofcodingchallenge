'''Python program to show the concept of mutation'''
if __name__=="__main__":
    items=(1,[4,5,6],"dhananjay",{1:"One",2:"Two"})
    print(items,type(items)) #(1, [4, 5, 6], 'dhananjay', {1: 'One', 2: 'Two'}) <class 'tuple'>
    #items[0]=2 #TypeError: 'tuple' object does not support item assignment
    #items[2][0]="D" #TypeError: 'str' object does not support item assignment
    items[1][0]="This will work"
    print(items) #(1, ['This will work', 5, 6], 'dhananjay', {1: 'One', 2: 'Two'})
    '''Whoo!! I am able to mutate a tuple object'''
    items[3][1]="This too"
    print(items)#(1, ['This will work', 5, 6], 'dhananjay', {1: 'This too', 2: 'Two'})
    '''Again i am able to mutate a tuple object. Actually, by definition, a tuple
    object is immutable meaning we can't change the tuple once we have created it.
    But the objects that a tuple object refers to are not immutable. In our case, tuple object
    refers to one list object, which is mutable, so, we are able to change the list object. But
    we can't assign a new list object to the tuple. That's the meaning of immutability in python
    context. Immutability is transitive in python. Beyond first level, it doesn't check for immutability'''
