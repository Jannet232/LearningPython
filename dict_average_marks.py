#STEP 1: Initialise name and score variable
student_name = ""
student_score = 0
more_input = "Yes"
#score_dict = {"":0}
score_dict=dict()

#Create a dictionary with student name and score.
#COntinue to append student names and scores until use does not want to enter any more data
while more_input == "Yes" or more_input == "Y" or more_input == "YES":
    student_name = input('Enter student name: ')
    student_score = int(input(f'How much did {student_name} score in Maths: '))
    print(f'{student_name} scored {student_score} in Maths.')
    score_dict[student_name] = student_score
    print(score_dict)
    more_input = input('Do you want to add another student\'s score? (Yes/No): ')
dict_sum = sum(score_dict.values())
dict_avg = dict_sum/len(score_dict)
#print(dict_sum)
#print(len(score_dict))
#print(dict_avg)
print(f'\nAverage marks in Maths for this class is {dict_avg}.')
