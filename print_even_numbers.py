#STEP 1: Input the first even number
first_num = int(input('Enter first number: '))

#STEP 2: Input how many even numbers needs to be printed
n = int(input('How many even numbers have to be printed?: '))

#STEP 3: Confirm the numbers entered by displaying it to the user
print(f'You want first {n} even numbers printed starting from {first_num}')

#STEP 5: If input number is even then start printing from that number else add 1 to the odd number to get nearest even number
if first_num % 2 == 0:
    nearest_even_number = first_num
elif first_num % 2 != 0:
    nearest_even_number = first_num + 1

#STEP 6: Print the range of even numbers
i = 0
for i in range(0,n):
    print(f"{nearest_even_number}")
    nearest_even_number += 2