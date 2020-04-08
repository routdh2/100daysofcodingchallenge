'''python program for making a calculator'''
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2==0:
        raise ValueError("Divide by zero.")
    else:
        return num1//num2
