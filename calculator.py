#Function to add two numbers
def add(a,b):
    return (a+b)

#Function to subtract two numbers
def subtract(a,b):
    if a > b:
        return (a-b)
    else:
        return (b-a)

#Function to multiply two numbers
def multiply(a,b):
    return (a*b)

#Function to divide two numbers
def divide(a,b):
    # If numerator is negative ask user to input a positive numerator
    if a < 0:
        print('Numerator is negative')
        a = int(input('Enter a numerator greater than 0: '))
    # If denominator is negative ask user to input a positive denominator
    elif b < 0:
        print('Denominator is negative')
        b = int(input('Enter a denominator greater than 0: '))
    # If denominator is equal to 0 ask user to input a positive denominator
    elif b == 0:
        print(f'Cannot divide {a} by 0')
        b = int(input('Enter a denominator greater than 0: '))

    return(a/b)

#Function to find the remainder
def remainder(a,b):
    # If numerator is negative ask user to input a positive numerator
    if a < 0:
        print('Numerator is negative')
        a = int(input('Enter a numerator greater than 0: '))

    # If denominator is negative ask user to input a positive denominator
    elif b < 0:
        print('Denominator is negative')
        b = int(input('Enter a denominator greater than 0: '))

    # If denominator is equal to 0 ask user to input a positive denominator
    elif b == 0:
        print(f'Cannot divide {a} by 0')
        b = int(input('Enter a denominator greater than 0: '))

    return(a%b)

#Function to find the quotient
def quotient(a,b):
    # If numerator is negative ask user to input a positive numerator
    if a < 0:
        print('Numerator is negative')
        a = int(input('Enter a numerator greater than 0: '))

    # If denominator is negative ask user to input a positive denominator
    elif b < 0:
        print('Denominator is negative')
        b = int(input('Enter a denominator greater than 0: '))

    # If denominator is equal to 0 ask user to input a positive denominator
    elif b == 0:
        print(f'Cannot divide {a} by 0')
        b = int(input('Enter a denominator greater than 0: '))

    return(a//b)

def square(a):
    # Find the square of the number
    return(num**2)

#Display options available in the calculator
print('(1) Add(+)')
print('(2) Subtract(-)')
print('(3) Multiply(*)')
print('(4) Divide(/)')
print('(5) Find Remainder (%)')
print('(6) Find Quotient (//)')
print('(7) Find Square of a number (**)')

#Accept option as input from user
option = int(input('Option Selected : '))


#Accept inputs based on mathematical operation to be performed
#User to input 2 numbers for add, subtract and multiply operation
if option in (1,2,3):
    # Input first number
    num1 = int(input('Enter first number: '))
    # Input second number
    num2 = int(input('Enter second number: '))
#After accepting 2 numbers call function for add (option = 1), subtract (option = 2), multiply (option 3)
    if option == 1:
        result = add(num1, num2)
    elif option == 2:
        result = subtract(num1, num2)
    elif option == 3:
        result = multiply(num1, num2)
#User to input 2 numbers for numerator and denominator to divide, to find remainder and to find the quotient
elif option in (4,5,6):
    # Input numerator
    num1 = int(input('Enter a number: '))
    # Input denominator
    num2 = int(input(f'Enter a number to divide {num1} with: '))
    if option == 4:
        result = divide(num1,num2)
    if option == 5:
        result = remainder(num1,num2)
    if option == 6:
        result = quotient(num1,num2)
#User to input the number to find the square of
elif option == 7:
    # Input the number
    num = int(input('Enter the number: '))
    result = square(num)
#If no valid options are chosen, print the message for user and exit the program without printing the result
else:
    print('Invalid option selected')
    exit()

#Print the result
print(f'Output is : {result}')
