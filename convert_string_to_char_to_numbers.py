#STEP 1: User to input string
input_string = input("Enter a string value: ")
print(f'You entered : {input_string} \n__________________________________________________')

#STEP 2: Print characters from input string
for c in input_string:
    print(c)

#STEP 3: Find length of string
length = len(input_string)

#STEP 4: Initialise variable for while loop and variable to save alphabet position for each character
position_string = ""
i = 0

#STEP 5: For each character in input_string, find the position in English alphabet and append it to variable saving
#postions. If the character is a space, append the space to the position variable
while i < length:
    if input_string[i] == ' ':
        position_string = position_string + ' '
    else:
        position_string = position_string + ' ' + str(format(ord(input_string[i].lower()) - 96))
    i += 1

print(f'String <{input_string}> after converting each characters to number is <{position_string}>')
