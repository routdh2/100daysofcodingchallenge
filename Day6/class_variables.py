#create a class Employee and show usage of class variables
class Employee:
    '''this is a class variable which is available across
    all its instances'''
    bonus_amount=10000
    def __init__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
    def showDetails(self):
        print([self.name,self.age,self.salary])
    def update_salary(self, amount):
        self.salary+=amount
    def display_bonus(self):
        print(self.bonus_amount) #it accesses class variable

emp1=Employee("Dhananjay",34,23000)
emp2=Employee("Tanmay",21,49909)
emp1.display_bonus()

print(Employee.__dict__)
emp1.bonus_amount=20000 #emp1 object has an extra attribute
print(Employee.bonus_amount) #it's still 10000
print(emp1.bonus_amount) #it accesses local attribute of object
print(emp2.__dict__)
