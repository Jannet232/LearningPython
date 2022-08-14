#This program will determine if a year input by the user is a Leap Year or Not

#Function to determine if year is divisible by 4 (remainder to be 0).

#STEP 1: Inform user about the functionality of the program
print('DETERMINE IF A YEAR IS A LEAP YEAR OR NOT')

#STEP 2: Initialise variable to continue in while to continue accepting year input from user until they exit
i = 'Y'

#STEP 3: Program will continue to remain in while loop asking for input from user until User inputs 'N'
while i == 'Y' or i == 'y':

    #STEP 4: Accept year as input from user and convert to int type
    year = int(input('Enter a Year : '))

    #STEP 5: Inform user that functionality is checking if year is leap year or not
    print(f'Checking if {year} is a leap year.')

    #STEP 6: Check if year is a century year by dividing by 100
    centremainder = year % 100
    #STEP 7: If year is a century year then if year is divisible by 400 it is a leap year
    #If year is not divisible by 400 then it is not a leap year
    if centremainder == 0:
        remainder = year % 400
        if remainder == 0:
            print(f'{year} is a leap year as its divisible by 400.')
        else:
            print(f'{year} is not a leap year as its divisible by 100 but not by 400.')
    #STEP 8: If year is not a century year then if year is divisible by 4 it is a leap
    #If year is not divisible by 4 then it is not a leap year
    else:
        remainder = year % 4
        if remainder == 0:
            print(f'{year} is a leap year as its divisible by 4 but not by 100 or 400.')
        else:
            print(f'{year} is not a leap as its not divisible by 4 or 400. ')

    #STEP 9: Ask user if they want to continue using the functionality for other years
    i = input(print('Do you want to use the functionality with another year (Y or N): '))
