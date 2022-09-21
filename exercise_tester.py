import pandas as pd
import random
import os
if not os.path.exists('testing'):
    with open('testing', 'w') as new_file:
        new_file.close()

TEST_DIFFICULTY = 0
WRITE_LOG = True

def choose_the_subject(subject_number):
    if subject_number == '1':
        import maths_exercises
        choose_the_subject.subject_exercises = maths_exercises
        choose_the_subject.subject_name = 'Maths'
    elif subject_number == '2':
        import russian_exercises
        choose_the_subject.subject_exercises = russian_exercises
        choose_the_subject.subject_name = 'Russian'
    elif subject_number == '3':
        import english_exercises
        choose_the_subject.subject_exercises = english_exercises
        choose_the_subject.subject_name = 'English'
    else:
        raise Exception(f'wrong Subject ID: {subject_number}')

# for i in range(1, len(exercises_list)):
#     if i < 10:
#         print(str(i) + '. ', exercises_list[i])
#     else:
#         print(str(i) + '.', exercises_list[i])

# exercise_number = input('Choose the exercise:  ')
# try:
#     exercise_number = int(exercise_number)
# except:
#     exercise_number = random.randint(1, len(exercises_list) - 1)
# exercise_name = exercises_list[exercise_number]
# os.system('cls' if os.name == 'nt' else 'clear')

with open('testing') as testing_save_file:
    testing = testing_save_file.read()
    testing_save_file.close()
backup_ok = False
subject_id = '1'
exercise_id = '1'
try:
    subject_id, exercise_id = testing.replace('\n', '').split(' ')
    backup_ok = True
except:
    print('         PROBLEM WITH READING THE PREVIOUS TEST NUMBER')

print('         PRESS ENTER TO CONTINUE WITH ' + testing)
print('         INPUT ANYTHING TO CHOOSE THE EXERCISE')
print('         IF YOU KNOW THE NUMBER, SPECIFY')
user_response = input()


if user_response:
    try:
        subject_id, exercise_id = [int(i) for i in user_response.split(' ')]
    except:
        print('Wrong input, we will do 1 1 then')
        user_exercise_selection_ok = False
    else:
        with open('testing', 'w') as testing_save_file:
            testing_save_file.write(f'{subject_id} {exercise_id}')
            testing_save_file.close()
        

choose_the_subject(subject_id)
subject_name = choose_the_subject.subject_name
subject_exercises = choose_the_subject.subject_exercises
os.system('cls' if os.name == 'nt' else 'clear')


# assigning exercise dictionary
exercises_dictionary = subject_exercises.exercises_dictionary
exercises_list = list(exercises_dictionary.keys())
# assigning exercise dictionary end

counter = 0
while True:
    counter += 1
    print(subject_id, subject_name, 'exercise', exercise_id)
    exercise = exercises_dictionary[exercises_list[int(exercise_id)]]['function']
    right_answers, input_message, prompt = exercise(difficulty=TEST_DIFFICULTY)
    print(input_message)
    print([i for i in right_answers])
    print('attempt number:', counter)
    if WRITE_LOG:
        log = open('test_log.csv', 'a')
        log.write(f"{pd.Timestamp.now()};{subject_id};{exercise_id};{input_message};{right_answers}\n")
    input()
