import os
import winsound
import random
import time


WIDTH = 40
HEIGHT = 4
ATTEMPTS = 3
FOLDER = 'materials/sample_texts/ru'
FILL = '_'
FILL_FRAC = 0.6

mistakes = 0
start = time.time()
text_name = random.choice(os.listdir(FOLDER))
text = list(open(f'{FOLDER}/{text_name}', encoding='utf-8'))


def good_job():
    winsound.Beep(1000, 80)
    winsound.Beep(1200, 50)


def bad_job():
    winsound.Beep(200, 300)
    winsound.Beep(170, 400)
    winsound.Beep(120, 1100)


def get_lines(paragraph, width):
    words = paragraph.split(' ')
    lines_good_to_go = []
    line = ''
    for word in words:
        if len(line) + len(word) <= width:
            line += word + ' '
        else:
            lines_good_to_go.append(line[:-1])
            line = word + ' '
    lines_good_to_go.append(line[:-1])
    return lines_good_to_go


def get_formatted(text, width=WIDTH) -> list:
    formatted_text = []
    for paragraph in text:
        paragraph = get_lines(paragraph, width)
        for p_line in paragraph:
            formatted_text.append(p_line.replace('\n', ''))
    return formatted_text


def prepare_word(
    word,
    fill: str = FILL,
    fill_frac: float =  FILL_FRAC
):
    if not word:
        return ''
    original = word
    word = word.replace('ться', f'т{fill}ся')
    word = word.replace('тся', f'т{fill}ся')
    if 'нн' in word:
        word = word.replace('нн', '(н/нн)')
    else:
        if word[0] != 'н':
            if word[-1] != 'н':
                word = word.replace('н', '(н/нн)')
    if 'сс' in word:
        word = word.replace('сс', '(с/сс)')
    else:
        if word[0] != 'с':
            if word[-1] != 'с':
                word = word.replace('с', '(с/сс)')
    len_ = len(word)
    if word.count(fill) >= len_ * fill_frac:
        return word
    if random.choice([0,1]):
        word = word.replace('ь', fill)
    if random.choice([0,1]):
        word = word.replace('ъ', fill)
    if random.choice([0,1]):
        word = word.replace('е', fill)
    if random.choice([0,1]):
        word = word.replace('и', fill)
    if random.choice([0,1]):
        word = word.replace('о', fill)
    if random.choice([0,1]):
        word = word.replace('а', fill)
    if word.count(fill) >= len_ * fill_frac:
        return prepare_word(
            original,
            fill=fill,
            fill_frac=fill_frac
        )
    return word


def prepare_line(line):
    line = line.split(' ')
    line = [prepare_word(word) for word in line]
    line = ' '.join(line)
    return line


formatted_text = get_formatted(text)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet += alphabet.upper()
alphabet += '0123456789'
max_len = len(formatted_text)
start_pos = 0
input_message = f' Greetings.\n There are {max_len} lines below.'
input_message += '\n Press ENTER to conquer them\n'
initial_input = input(input_message)
try:
    if initial_input.isnumeric():
        initial_input = int(round(float(initial_input)))
        if 0 <= initial_input < max_len:
            start_pos = initial_input
except:
    pass

current_pos = start_pos
while current_pos <= max_len:
    first_line_is_okay = False
    glitch_plug_counter = 100
    while not first_line_is_okay:
        first_line = formatted_text[current_pos]
        glitch_plug_counter -= 1
        if not glitch_plug_counter:
            raise Exception('First line never in alphabet')
        #if 's' in first_line:
        if len(first_line) > 1:
            for char in first_line:
                if char in alphabet:
                    first_line_is_okay = True
        if not first_line_is_okay:
            current_pos += 1

    from_ = current_pos
    to_ = current_pos + HEIGHT
    if to_ > max_len:
        to_ = max_len
    text_to_show = formatted_text[from_: to_]

    os.system('cls')
    delta = int(time.time() - start)
    delta = f'{delta // 60}:{str(delta % 60).zfill(2)}'
    top_line = f'Line {current_pos + 1}: {round(100 * current_pos / max_len, 1)}%'
    top_line += ' ' * 10
    top_line += f'Mistakes: {mistakes}  Time: {delta}'
    print(top_line)
    print('\n' * 4)
    for line in text_to_show:
        print(prepare_line(line))
    prompt = '\n>>> Напечатай первую строчку, вставляя буквы по необходимости:\n\n'

    attempts_rem = ATTEMPTS
    for attempt in range(ATTEMPTS):
        input_ = input(prompt)
        if input_ == first_line:
            good_job()
            break
        else:
            attempts_rem -= 1
            mistakes += 1
            bad_job()
            print('\nThe correct answer was:')
            print(first_line)
            input(f'\nPress ENTER and try again. Attempts: {attempts_rem}')
    current_pos += 1
os.system('cls')
print('\n' * 4)
print(f'{max_len} lines complete!')
print('\n' * 4)
print('Good job.')
print('If you are reading this, your my personal hero.')
print()
input('Press Enter to EXIT')







