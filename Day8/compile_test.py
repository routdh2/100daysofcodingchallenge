'''program to check whether python is interpreted
or compile time language'''
if __name__=="__main__":
    string="dhananjay"
    def func1(string):
        print("Hello",string)
    if string=="Guido":
        func2(string) #although func2 is never defined, but python didn't raise any error
    else:
        func1(string)
    def add(num1,num2):
        return num1+num2
    add("dbdd",3) #throws error at runtime not at compile time
