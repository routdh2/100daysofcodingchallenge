'''Program to display the usage of class variables
and class methods'''
if __name__=="__main__":
    class Employee:
        bonus_amount=1000
        def __init__(self,name,age,salary):
            self.name=name
            self.age=age
            self.salary=salary
        def show_details(self):
            print([self.name,self.age,self.salary])
        @classmethod
        def set_bonus_amount(cls,amount):
            cls.bonus_amount=amount

    emp1=Employee("Dhananjay",23,39940)
    emp2=Employee("Tanmay",43,993883)
    print(emp1.bonus_amount) #prints 1000
    Employee.set_bonus_amount(2000)
    print(emp1.bonus_amount) #prints 2000
    print(Employee.bonus_amount) #prints 2000
    emp1.bonus_amount=500
    emp1.set_bonus_amount(3000) #we can use object to call classmethod but that changes the class var only
    print(Employee.bonus_amount)#still prints 3000
    print(emp1.__dict__)
    print(emp1.bonus_amount) #prints 500
