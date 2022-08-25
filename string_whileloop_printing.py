#STEP 1: User to input string
input_string = input("Enter a string value: ")
print(f'You entered : {input_string} \n__________________________________________________')

#STEP 2: Find length of string
length = len(input_string)

#STEP 3: Initialise variable for loop
i = 0
print(f'Printing characters of {input_string} ')

#STEP 4: Print every character in the string
while i < length:
    char = input_string[i]
    print(char)
    i += 1

#STEP 5: Initialise variable for loop to the length of the string
i = length - 1
print(f'Printing characters of {input_string}  in reverse')

#STEP 6: Print every character in the string in reverse order
while i >= 0:
    char = input_string[i]
    print(char)
    i -= 1
