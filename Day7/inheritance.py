'''program to show the use of inheritance in python'''
if __name__=="__main__":
    class Employee:
        bonus_amount=100
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def show_details(self):
            print([self.name,self.age])

    class Developer(Employee):
        def __init__(self,name,age,prog_lang):
            super().__init__(name,age)
            #Employee.__init__(self,name,age)
            self.prog_lang=prog_lang
        def set_bonus(self,amount):
            self.bonus_amount=amount
    class Manager(Employee):
        def __init__(self,name,age,employees=None):
            super().__init__(name,age)
            if employees is None:
                self.employees=[]
            else:
                self.employees=employees
        def add_emp(self,emp):
            if emp not in self.employees:
                self.employees.append(emp)
        def remove_emp(self,emp):
            if emp in self.employees:
                self.employees.remove(emp)
        def list_emps(self):
            for emp in self.employees:
                emp.show_details()
    emp1=Employee("Dhananjay",23)
    print(emp1)
    dev1=Developer("Dhananjay",23,"python")
    dev2=Developer("tanmay",34,"Java")
    dev1.show_details()
    dev1.set_bonus(2300)
    print(dev1.bonus_amount)
    # print(help(dev1))
    print(emp1.bonus_amount)
    print(isinstance(dev1,Employee))
    print(issubclass(Employee,Developer))
    mgr1=Manager("Arvind",34,[dev1])
    print(mgr1.bonus_amount)
    mgr1.list_emps()
    mgr1.add_emp(dev2)
    mgr1.list_emps()
    mgr1.remove_emp(dev1)
    mgr1.list_emps()
    print(issubclass(Manager,Developer))
