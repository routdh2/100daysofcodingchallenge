'''Count no of employees in a company'''
class Employee:
    '''this is a class variable which is available across
    all its instances'''
    no_of_emps=0
    def __init__(self,name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary
        Employee.no_of_emps+=1
    def showDetails(self):
        print([self.name,self.age,self.salary])
    def update_salary(self, amount):
        self.salary+=amount

emp1=Employee("Dhananjay",34,23000)
emp2=Employee("Tanmay",21,49909)
print(Employee.__dict__)
print(emp1.__dict__)
print(Employee.no_of_emps)
print(emp1.no_of_emps)

