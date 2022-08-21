#STEP 1: User to input string
input_string = input("Enter a string value: ")
print(f'You entered : {input_string} \n__________________________________________________')

#STEP 2: Print first character in string
first_char = input_string[0]
print(f"""First character in '{input_string}' is {first_char} \n__________________________________________________""")

#STEP 3: Find length of string
length = len(input_string)

#STEP 4: Print last character in string
last_char = input_string[length - 1]
print(f"""Last character in '{input_string}' is {last_char} \n____________________________________________________""")

#STEP 5: Print length of string from STEP 3
print(f"""Length of string '{input_string}' is {length} \n________________________________________________________""")

#STEP 6: Find middle index of string
mid_index = int(length/2)
print(f"""Mid index is {mid_index} \n________________________________________________________""")

#STEP 7: Print middle characters in string
#If length of string is even then print both the middle characters
#If length of string is odd then print the single middle character
if length % 2 == 0:
    mid_character_1 = input_string[mid_index - 1]
    mid_character_2 = input_string[mid_index]
    print(f"""Middle characters in '{input_string}' are {mid_character_1} and {mid_character_2}  \n________________________________________________________""")
elif length % 2 != 0:
    mid_character = input_string[mid_index]
    print(
        f"""Middle character in '{input_string}' is {mid_character}  \n________________________________________________________""")
