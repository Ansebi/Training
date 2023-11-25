import os
import winsound

WIDTH = 40
HEIGHT = 4
ATTEMPTS = 3

text = os.listdir('sample_texts')[0]
text = open(f'sample_texts/{text}', encoding='utf-8')
text = [i for i in text]


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


def get_formatted(text) -> list:
    formatted_text = []
    for paragraph in text:
        paragraph = get_lines(paragraph, WIDTH)
        for p_line in paragraph:
            formatted_text.append(p_line.replace('\n', ''))
    return formatted_text


formatted_text = get_formatted(text)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()
alphabet += '0123456789'

max_len = len(formatted_text)

start_pos = 0
initial_input = input(f' Greetings.\n There are {max_len} lines below.\n Press ENTER to conquer them\n')
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
    print(f'{round(100*current_pos/max_len, 1)}%')
    print('\n'*4)
    for line in text_to_show:
        print(line.replace('s', ''))
    prompt = '\n>>> Type the first line, adding "s" if needed:\n\n'

    attempts_rem = ATTEMPTS
    for attempt in range(ATTEMPTS):
        input_ = input(prompt)
        if input_ == first_line:
            good_job()
            break
        else:
            attempts_rem -= 1
            bad_job()
            print('\nThe correct answer was:')
            print(first_line)
            input(f'\nPress ENTER and try again. Attempts: {attempts_rem}')
    current_pos += 1
os.system('cls')
print('\n'*4)
print(f'{max_len} lines complete!')
print('\n'*4)
print('Good job.')
print('If you are reading this, your my personal hero.')
print()
input('Press Enter to EXIT')







