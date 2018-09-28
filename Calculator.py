"""
*Project: THE PROGRAMIMG CALCULATOR
*Programmer: Tyler Muranaka
*Version: 1.5
"""

#Menu screen
print("""
Welcome to The Programming Calculator!!! \n
Type one:
*Addition()
*Subtraction()
*Multiplication()
*Division()
*Modulo()
""")

#Addition
def Addition():
    first = int(input('What is your first number'))
    second = int(input('What is your second number.'))
    print(first + second)
    
#Subtraction
def Subtraction():
    first = int(input('What is your first number?'))
    second = int(input('What is your second number?'))
    print(first - second)
 
#Multiplication 
def Multiplication():
    first = int(input('What is your first number?'))
    second = int(input('What is your second number?'))
    print(first * second)
    
#Division
def Division():
    first = int(input('What is your first number?'))
    second = int(input('What is your second number?'))
    print(first / second)
    
#Modulo
def Modulo():
    first = int(input('What is your first number?'))
    second = int(input('What is your second number?'))
    print(first % second)