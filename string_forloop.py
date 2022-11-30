#STEP 1: User to input string
input_string = input("Enter a string value: ")
print(f'You entered : {input_string} \n__________________________________________________')

#STEP 2: Find length of string
length = len(input_string)

#STEP 3: Print characters from input string
for c in input_string:
    print(c)

#STEP 4: Reverse input string
rev_string = ""
for r in input_string:
    rev_string = r + rev_string

rev_string_2 = input_string[::-1]

#STEP 5: Print characters from reversed string
print(f'First reverse printing \n__________________________________________________')
for c2 in rev_string:
    print(c2)

print(f'Second reverse printing \n__________________________________________________')
for c3 in rev_string_2:
    print(c3)
