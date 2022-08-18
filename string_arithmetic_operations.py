#STEP 1: User to input first string
first_string = input("Enter a string value: ")

#STEP 2: User to input second string
second_string = input("Enter another string value: ")

#STEP 3: User to input the number of times string must be repeated and printed
num = int(input("Enter a number (preferable less than 10: "))

#STEP 4: Print number input by user
print(f'You entered number: {num}')
print("------------------------------------")

#STEP 5: Concatenate the two strings and print
comb_string = first_string + second_string
print(f'{first_string} + {second_string} is {comb_string}')
print("------------------------------------")

#STEP 6: Repeat first_string for num number of times
repeat_first_string = first_string * num
print(f'{first_string} * {num} is {repeat_first_string}')
print("------------------------------------")

#STEP 7: Repeat second_string for num number of times
repeat_second_string = second_string * num
print(f'{second_string} * {num} is {repeat_second_string}')
print("------------------------------------")
