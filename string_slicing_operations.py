#STEP 1: User to input string
input_string = input("Enter a string value: ")
print(f'You entered : {input_string} \n__________________________________________________')

#STEP 2: Find length of string
length = len(input_string)

#STEP 3: Slice of the string after removing first(f) and last(l) character
slice_fl = input_string[1:-1]
print(f"""Slice of '{input_string}' after removing first and last characters is '{slice_fl}' \n__________________________________________________""")

#STEP 4: Slice of string after removing the first 2 characters (f2)
slice_f2 = input_string[2:length]
print(f"""Slice of '{input_string}' after removing first 2 characters is '{slice_f2}' \n__________________________________________________""")

#STEP 5: Slice of string after removing the last 2 characters (l2)
slice_l2 = input_string[0:-2]
print(f"""Slice of '{input_string}' after removing last 2 characters is '{slice_l2}' \n__________________________________________________""")

#STEP 6: Find middle index of string
mid_index = int(length/2)
print(f"""Mid index is {mid_index} \n________________________________________________________""")

#STEP 7: Print middle characters in string
#If length of string is even slice the string into 2 equal parts
#If length of string is odd then second slice has will have one character more than the first
slice_1 = input_string[0:mid_index]
slice_2 = input_string[mid_index:length]
print(f"""First half slice of '{input_string}' is '{slice_1}'""")
print(f"""Second half slice of '{input_string}' is '{slice_2}'  \n________________________________________________________""")

