import random
import os

def choose_the_subject(subject_number):
    if subject_number == '1':
        import maths_exercises
        choosing_the_subject.subject_exercises = maths_exercises
        choosing_the_subject.subject_name = 'Maths'
    elif subject_number == '2':
        import russian_exercises
        choosing_the_subject.subject_exercises = russian_exercises
        choosing_the_subject.subject_name = 'Russian'
    elif subject_number == '3':
        import english_exercises
        choosing_the_subject.subject_exercises = english_exercises
        choosing_the_subject.subject_name = 'English'
    else:
        subject_number = random.choice(['1', '2', '3'])
        choose_the_subject(subject_number)


choose_the_subject(subject_number)
subject_exercises = choose_the_subject.subject_exercises
subject_name = choose_the_subject.subject_name
os.system('cls' if os.name == 'nt' else 'clear')
### CHOOSE THE SUBJECT END

# assigning exercise dictionary
exercises_dictionary = subject_exercises.exercises_dictionary
exercises_list = subject_exercises.exercises_list
# assigning exercise dictionary end

for i in range(1, len(exercises_list)):
    if i < 10:
        print(str(i) + '. ', exercises_list[i])
    else:
        print(str(i) + '.', exercises_list[i])

exercise_number = input('Choose the exercise:  ')
try:
    exercise_number = int(exercise_number)
except:
    exercise_number = random.randint(1, len(exercises_list) - 1)
exercise_name = exercises_list[exercise_number]
os.system('cls' if os.name == 'nt' else 'clear')



print('\n' * 8 + '         PRESS ENTER TO CONTINUE WITH ' + testing + '\n' * 10)
print('\n' * 8 + '         INPUT ANYTHING TO CHOOSE THE EXERCISE' + '\n' * 10)
print('\n' * 8 + '         IF YOU KNOW THE NUMBER, SPECIFY' + '\n' * 10)
user_response = input()

if not user_response:
    if not os.path.exists('testing'):
        with open('testing', 'w'):
            pass

    with open('testing', 'r') as testing_backup:
        testing = testing_backup.read()
        testing_backup.close()
    subject_number = testing.replace('\n', '').split(' ')[0]
    exercise_number = testing.replace('\n','').split(' ')[1]

