# import libraries:
import winsound
import time
import random
import os
import sys
import datetime
# import modules:
import image_module
import maths_exercises
import russian_exercises
import english_exercises
from score_counter import score_counter

# import data_fixer

DEFAULT_TARGET_SCORE = 1000
DEFAULT_FIXED_TIME_SEC = 60
DEFAULT_FIXED_NUMBER_OF_TASKS = 15


def global_():
    pass


def start():
    global_.start = datetime.datetime.now()
    global_.start_simple_time_format = time.time()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_type(exercise_name, difficulty):
    print(exercise_name, '\n')
    difficulty_repr = difficulty if difficulty else 'Normal'
    print(f'Difficulty Level: {difficulty_repr}')
    print('to change the difficulty, set the desired level, e.g. "set 5"')
    print('\n')
    print('1. Fixed number of tasks')
    print('2. Fixed time')
    print('3. Target score')
    training_type = input('Choose the type of training: ')
    clear()
    return training_type


def core(the_exercise, difficulty, standard_completion_time_sec):
    right_answers, input_message, prompt = the_exercise(difficulty)
    right_answers = [str(i) for i in right_answers]
    print(f"points: {global_.score}       accuracy: {global_.percentage}%")
    print('\n')
    if prompt:
        print(prompt)
    ans = input(input_message)

    if ans in right_answers:
        global_.correct += 1
        winsound.Beep(1000, 80)
        image_module.congrats()
        winsound.Beep(1200, 50)
        input('\nWell done :) Press ENTER\n')
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        global_.incorrect += 1
        winsound.Beep(200, 300)
        winsound.Beep(170, 400)
        image_module.lose()
        winsound.Beep(120, 1100)

        os.system('cls' if os.name == 'nt' else 'clear')
        print('points:', global_.score, end='')
        print('       accuracy:', global_.percentage, '%', '\n' * 2)
        print('the correct answer is:')
        right_answer = right_answers[0]
        print(input_message + str(right_answer))
        print('\n')
        input('Try again :( Press ENTER\n')
        os.system('cls' if os.name == 'nt' else 'clear')

    global_.percentage = round((global_.correct / (global_.correct + global_.incorrect) * 100), 1)
    global_.minutes_elapsed = int(str(datetime.datetime.now() - global_.start)[2:4])
    global_.seconds_elapsed = int(round(float(str(datetime.datetime.now() - global_.start)[5:10]), 0))

    score = score_counter(
        standard_completion_time_sec,
        global_.percentage,
        global_.minutes_elapsed,
        global_.seconds_elapsed,
        global_.correct,
        global_.incorrect)
    global_.score = score
    global_.time_elapsed = time.time() - global_.start_simple_time_format
    

def training():
    """ENTRANCE"""
    if not os.path.exists('last_user'):
        with open('last_user', 'w'):
            pass
    with open('last_user', 'r') as last_user_backup:
        last_user = last_user_backup.read()
        print('\n' * 8 + '         Hello, ' + last_user + '!' + '\n' * 10)
        last_user_backup.close()
    user_name = input('PRESS ENTER\nor sign as a different fighter: ')
    if not user_name:
        user_name = last_user
    else:
        with open('last_user', 'w') as last_user_backup:
            last_user_backup.write(user_name)
            last_user_backup.close()
    print('Okay,', user_name)
    time.sleep(0.3)
    clear()
    """ENTRANCE END"""

    """CHOOSE THE SUBJECT"""
    dict_subjects = {'1': {'subject_exercises': maths_exercises,
                           'subject_name': 'Maths'},
                     '2': {'subject_exercises': russian_exercises,
                           'subject_name': 'Russian'},
                     '3': {'subject_exercises': english_exercises,
                           'subject_name': 'English'}}
    print('\n' * 8 + '         ' + user_name + ', please choose the subject:' + '\n')
    for n, val in dict_subjects.items():
        print(f"{n}. {val['subject_name']}")
    print('\n' * 4)
    subject = input('Your choice:  ')

    if subject not in dict_subjects:
        subject = random.choice(list(dict_subjects.keys()))
    subject_name = dict_subjects[subject]['subject_name']
    subject_exercises = dict_subjects[subject]['subject_exercises']
    clear()
    """CHOOSE THE SUBJECT END"""

    # assign exercise dictionary
    exercises_dictionary = subject_exercises.exercises_dictionary
    exercises_list = list(exercises_dictionary.keys())

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
    difficulty = exercises_dictionary[exercise_name]['default_difficulty']
    standard_completion_time_sec = exercises_dictionary[exercise_name]['standard_completion_time_sec']
    clear()



    # constants
    global_.time_elapsed = 0
    global_.correct = 0
    global_.incorrect = 0
    global_.fixed_time = DEFAULT_FIXED_TIME_SEC
    global_.number_of_tasks = DEFAULT_FIXED_NUMBER_OF_TASKS
    global_.percentage = 0
    global_.score = 0

    the_exercise = exercises_dictionary[exercise_name]['function']
    training_type = choose_type(exercise_name, difficulty)
    if 'set' in training_type:
        try:
            _, difficulty = training_type.split(' ')
            difficulty = int(difficulty)
        except:
            difficulty = 0
        training_type = choose_type(exercise_name, difficulty)

    if training_type == '3':
        global_.target_score_input = input('Specify the target score: ')
        try:
            global_.target_score = int(global_.target_score_input)
        except:
            global_.target_score = DEFAULT_TARGET_SCORE
        clear()
        start()
        while global_.score < global_.target_score:
            print(exercise_name, '    ', end='')
            print('score:', str(global_.score) + '/' + str(global_.target_score))
            core(the_exercise, difficulty, standard_completion_time_sec)
    elif training_type == '2':
        global_.fixed_time_input = input('Specify the time for training (minutes): ')
        if global_.fixed_time_input != '':
            global_.fixed_time = float(global_.fixed_time_input) * 60  # it's in seconds
        clear()
        start()
        while global_.time_elapsed < global_.fixed_time:
            time_remaining = global_.fixed_time - global_.time_elapsed
            seconds_remaining = time_remaining % 60
            minutes_remaining = int((time_remaining - seconds_remaining) / 60)
            seconds_remaining = int(round(seconds_remaining, 0))
            print(exercise_name, '    ', end='')
            print('time remaining:', str(minutes_remaining) + ':' + str(seconds_remaining))
            core(the_exercise, difficulty, standard_completion_time_sec)
    else:
        global_.number_of_tasks_input = input('Specify the number of tasks: ')
        if global_.number_of_tasks_input != '':
            global_.number_of_tasks = int(global_.number_of_tasks_input)
        clear()
        start()
        for i in range(global_.number_of_tasks):
            print(exercise_name, '    ', end='')
            print('tasks complete:', str(i) + '/' + str(global_.number_of_tasks))
            core(the_exercise, difficulty, standard_completion_time_sec)

    print(exercise_name, '\n')
    print(global_.percentage, '%')
    print(global_.minutes_elapsed, 'min', global_.seconds_elapsed, 'sec')
    print(global_.correct, 'out of', global_.correct + global_.incorrect, '\n')
    print('Your score:', global_.score, '\n')
    image_module.numeric_display(global_.score)

    file_name = 'data_' + user_name + '.csv'
    data = open(file_name, 'a')
    data.write(str(datetime.datetime.now())[0:4] + ';')
    data.write(str(datetime.datetime.now())[5:7] + ';')
    data.write(str(datetime.datetime.now())[8:10] + ';')
    data.write(str(datetime.datetime.now())[11:19] + ';')
    data.write(subject_name + ';')
    data.write(str(str(exercise_name) + ';'))
    data.write(str(str(difficulty) + ';'))
    data.write(str(str(global_.minutes_elapsed) + ';min;' + str(global_.seconds_elapsed) + ';sec;'))
    data.write(str(str(global_.correct) + ';/;' + str(global_.incorrect + global_.correct) + ';'))
    data.write(str(str(global_.percentage) + '%;' + str(global_.score) + ';\n'))
    data.close()

    print()
    exit_input = input('PRESS ANY KEY TO CONTINUE\n')
    if exit_input.lower() in [
        'bye', 'see ya', 'exit', 'goodbye', 'hasta la vista', 'farewell', 'dosviduli', 'off', 'finish']:
        sys.exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


while True:
    training()
