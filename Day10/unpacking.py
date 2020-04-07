'''Program to leran how unpacking works in python'''
if __name__=="__main__":
    a=(2,3)
    print(a,type(a))
    a,b=(2,3)
    print(a,b) #prints 2 3
    a,b,*c=[1,2,3,4,5]
    print(a,b,c) #prints 1 2 [3,4,5]
    a,b,*_=(1,2,3,4,5)
    print(a,b) #prints 1 2
    a,b,*c,d=(1,2,3,4,5,6)
    print(a,b,c,d) #prints 1 2 [3,4,5] 6
