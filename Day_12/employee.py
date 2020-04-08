'''Program to create an Employee class for unittesting'''
class Employee:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
    def get_email(self):
        return "{}.{}@email.com".format(self.first,self.last)
    def get_fullname(self):
        return "{} {}".format(self.first,self.last)
