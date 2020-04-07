'''Part 2 of useful python commands'''
if __name__=="__main__":
    '''1. setattr() and getattr() method'''
    class Employee:
        pass
    emp1=Employee()
    emp1.name="Dhananjay"
    emp1.age=23
    print(emp1.name,emp1.age)
    key1="salary"
    val1=34000
    #how to set this attribute to our emp object
    setattr(emp1,key1,val1)
    print(getattr(emp1,key1))

    '''setattr() is used to set the attribute to an object
    getattr() is used to get the value of an attribute'''
    response={"name":"Dhananjay","age":30,"salary":543}
    for key,value in response.items():
        setattr(emp1,key,value)
    for key in response.keys():
        print(getattr(emp1,key))
