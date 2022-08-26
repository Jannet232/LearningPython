#STEP 1: Input the first number
first_num = int(input('Enter first number: '))
print(f'You entered : {first_num} \n__________________________________________________')

#STEP 2: Input how many odd numbers needs to be printed
n = int(input('How many odd numbers have to be printed?: '))

#STEP 3: Confirm the numbers entered by displaying it to the user
print(f'__________________________________________________'
      f'\n You want first {n} odd numbers printed starting from {first_num}'
      f'\n__________________________________________________')

#STEP 5: If input number is even then start printing from that number else add 1 to the odd number to get nearest even number
if first_num % 2 == 0:
    nearest_odd_number = first_num + 1
    nearest_odd_number_2 = first_num + 1
elif first_num % 2 != 0:
    nearest_odd_number = first_num
    nearest_odd_number_2 = first_num

#STEP 6: Print the range of odd numbers
print(f'Print using for loop and range method \n__________________________________________________')
i = 0
for i in range(0,n):
    print(f"{nearest_odd_number}")
    nearest_odd_number += 2

#STEP 7: Print using while loop
print(f'__________________________________________________'
      f'\nPrint using while loop \n__________________________________________________')
i = 0
while i < n:
    print(f"{nearest_odd_number_2}")
    nearest_odd_number_2 += 2
    i +=1