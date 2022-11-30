def fibonacci(x,y,cnt):
    i = 0
    for i in range(x,cnt):
        z = x+y
        x = y
        y = z
        print(z)


#STEP 1: Input the first number
first_num = int(input('Enter first number: '))
print(f'You entered : {first_num} \n__________________________________________________')

#STEP 2: Input how many fibonacci numbers needs to be printed
count = int(input('How many Fibonacci numbers have to be printed?: '))

#STEP 3: Confirm the numbers entered by displaying it to the user
print(f'__________________________________________________'
      f'\n Printing first {count} Fibonacci numbers after {first_num}'
      f'\n__________________________________________________')

#STEP 4: Initialise first 2 numbers in Fibonacci series
a = 0
b = 1

#STEP 5: In Fib series, Fib(n) = Fib(n-1)_ + Fib(n-2)
#If first_num entered is 0, next number to printed is 1
if first_num == 0 and count == 1:
    print(b)
elif first_num == 0 and count > 1:
    print(b)
    count -= 1
    fibonacci(a,b,count)
#else:
#    fib(first_num,n)