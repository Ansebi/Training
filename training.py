repeat = True
while repeat:
    import winsound
    import time
    import random
    import os
    import datetime
    import image_module
    # import data_fixer
    import sys


    def global_():
        pass


### ENTRANCE
    if not os.path.exists('last_user'):
        with open('last_user', 'w'):
            pass

    with open('last_user', 'r')as last_user_backup:
        last_user = last_user_backup.read()
        print('\n' * 8 + '         Hello, ' + last_user + '!' + '\n' * 10)
        last_user_backup.close()
    user_switcher = 'OFF'
    user_name = input('PRESS ENTER\nor sign as a different fighter: ')
    if user_name == '' or user_name == last_user:
        user_name = last_user
    else:
        with open('last_user', 'w')as last_user_backup:
            last_user_backup.write(user_name)
            last_user_backup.close()
    print('Okay,', user_name)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
### ENTRANCE END

### CHOOSE THE SUBJECT
    print('\n' * 8 + '         ' + user_name + ', please choose the subject:' + '\n')
    print('1. Maths')
    print('2. Russian')
    print('3. English')
    print('\n' * 4)
    subject = input('Your choice:   ')

    def choosing_the_subject(subject):
        if subject == '1':
            import maths_exercises
            choosing_the_subject.subject_exercises = maths_exercises
            choosing_the_subject.subject_name = 'Maths'
        elif subject == '2':
            import russian_exercises
            choosing_the_subject.subject_exercises = russian_exercises
            choosing_the_subject.subject_name = 'Russian'
        elif subject == '3':
            import english_exercises
            choosing_the_subject.subject_exercises = english_exercises
            choosing_the_subject.subject_name = 'English'
        else:
            subject = random.choice(['1','2','3'])
            choosing_the_subject(subject)


    choosing_the_subject(subject)
    subject_exercises =  choosing_the_subject.subject_exercises
    subject_name = choosing_the_subject.subject_name
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

    print(exercise_name, '\n')
    print('1. Fixed number of tasks')
    print('2. Fixed time')
    print('3. Target score')
    training_type = input('Choose the type of training: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    # constants
    global_.time_elapsed = 0
    global_.correct = 0
    global_.incorrect = 0
    global_.fixed_time = 60
    global_.number_of_tasks = 15
    global_.percentage = 0
    global_.score = 0
    constants = []


    # constants end

    def start():
        global_.start = datetime.datetime.now()
        global_.start_simple_time_format = time.time()


    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    # core process definition
    def core():
        the_exercise = exercises_dictionary[exercise_name]

        # the core of the core defined:
        def the_core_of_the_core():

            the_exercise()

            print('points:', global_.score, end='')
            print('       accuracy:', global_.percentage, '%', '\n' * 2)
            try:
                print(subject_exercises.prompt)
            except:
                pass

            # ans=maths_exercises.ans
            ans = input(subject_exercises.input_message)
            right_answers = subject_exercises.right_answers
            input_message = subject_exercises.input_message

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
                if type(right_answers[0]) == float:
                    if right_answers[0] % 1 == 0:
                        right_answer = int(right_answers[0])
                    else:
                        right_answer = right_answers[0]
                else:
                    right_answer = right_answers[0]
                print(input_message + str(right_answer))
                print()

                input('\nTry again :( Press ENTER\n')
                os.system('cls' if os.name == 'nt' else 'clear')

            global_.percentage = round((global_.correct / (global_.correct + global_.incorrect) * 100), 1)

            global_.minutes_elapsed = int(str(datetime.datetime.now() - global_.start)[2:4])
            global_.seconds_elapsed = int(round(float(str(datetime.datetime.now() - global_.start)[5:10]), 0))

            import score_counter
            score_counter = score_counter.score_counter
            score_counter(
                global_.score,
                global_.percentage,
                global_.minutes_elapsed,
                global_.seconds_elapsed,
                global_.correct,
                global_.incorrect)
            global_.score = score_counter.score

            global_.time_elapsed = time.time() - global_.start_simple_time_format

        # the core of the core defined end

        print(exercise_name, '\n')
        if training_type == '3':
            global_.target_score_input = input('Specify the target score: ')
            try:
                global_.target_score = int(global_.target_score_input)
            except:
                global_.target_score = 1000

            clear()
            start()
            while global_.score < global_.target_score:
                print(exercise_name, '    ', end='')
                print('score:', str(global_.score) + '/' + str(global_.target_score))

                the_core_of_the_core()

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
                the_core_of_the_core()

        else:
            global_.number_of_tasks_input = input('Specify the number of tasks: ')
            if global_.number_of_tasks_input != '':
                global_.number_of_tasks = int(global_.number_of_tasks_input)
            clear()
            start()
            for i in range(global_.number_of_tasks):
                print(exercise_name, '    ', end='')
                print('tasks complete:', str(i) + '/' + str(global_.number_of_tasks))
                the_core_of_the_core()


    # core process definition end
    core()

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
    data.write(str(str(global_.minutes_elapsed) + ';min;' + str(global_.seconds_elapsed) + ';sec;'))
    data.write(str(str(global_.correct) + ';/;' + str(global_.incorrect + global_.correct) + ';'))
    data.write(str(str(global_.percentage) + '%;' + str(global_.score) + ';\n'))
    data.close()

    print()
    # input('PRESS ENTER TO CONTINUE')
    exit_input = input('PRESS ANY KEY TO CONTINUE\n')
    if exit_input in ['bye', 'see ya', 'exit', 'EXIT', 'Goodbye', 'Hasta la vista', 'farewell', 'Hasta la vista',
                      'dosviduli']:
        sys.exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
