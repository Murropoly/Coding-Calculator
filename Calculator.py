"""
*Project: THE PROGRAMIMG CALCULATOR
*Programmer: Tyler Muranaka
*Version: 2.0
"""

#Menu screen
print("""
Welcome to The Programming Calculator!!!\n
Type one:
*Addition()
*Subtraction()
*Multiplication()
*Division()
*Modulo()
""")

#Addition
def Addition():
    first = int(input("Type First Number: "))
    second = int(input("Type Second Number: "))
    print(first + second)
    
#Subtraction
def Subtraction():
    first = int(input("Type First Number: "))
    second = int(input("Type Second Number: "))
    print(first - second)
 
#Multiplication 
def Multiplication():
    first = int(input("Type First Number: "))
    second = int(input("Type Second Number: "))
    print(first * second)
    
#Division
def Division():
    first = int(input("Type First Number: "))
    second = int(input("Type Second Number: "))
    print(first / second)
    
#Modulo
def Modulo():
    first = int(input("Type First Number: "))
    second = int(input("Type Second Number: "))
    print(first % second)
