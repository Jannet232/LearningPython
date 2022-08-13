#This program will determine if a year input by the user is a Leap Year or Not

#Function to determine if year is divisible by 4 (remainder to be 0).
# If remainder is 0, year is a Leap Year, so return True.
# If remainder is not 0, year is not a leap Year, so return False.
def divby4(a):
    remainder = a%4
    if remainder == 0:
        return True
    else:
        return False

#STEP 1: Inform user about the functionality of the program
print('DETERMINE IF A YEAR IS A LEAP YEAR OR NOT')

#STEP 2: Initialise variable to continue in while to continue accepting year input from user until they exit
i = 'Y'

#STEP 3: Program will continue to remain in while loop asking for input from user until User inputs 'N'
while i == 'Y' or i == 'y':

    #STEP 4: Accept year as input from user and convert to int type
    year = int(input('Enter a Year : '))

    #STEP 5: Check if number input is a year with 4 digits
    length = len(str(year))
    if length != 4:
        year = int(input('Invalid Year. Enter a 4 digit Year: '))

    #STEP 5: Inform user that functionality is checking if year is leap year or not
    print(f'Checking if {year} is a leap year.')

    #STEP 6: Call function to determine if the year is a leap year or not.
    #Print result for user
    if divby4(year):
       print(f'{year} is a leap year as it is divisible by 4')
    else:
       print(f'{year} is not a leap year as it is not divisible by 4')

    #STEP 7: Ask user if they want to continue using the functionality for other years
    i = input(print('Do you want to use the functionality with another year (Y or N): '))
