number = '3.6999999999999997'

MAX_REPS = 4
number = float(number)

import re

class NotInRangeError(Exception):
    '''the value is not supported (too large or too small)'''

    def __init__(self, message= 'the value has to be between 10**-13 and 10**13'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

if not 10**-13 < number < 10**13:
    raise NotInRangeError

magnitude = None
for power in range(-13, 14):
    print(10**power, number)
    if 10**power > number:
        magnitude = power - 1
        break

number_string = str(number)#.replace('.','')

prev_digit = ''
counter = 1
round_pos = None
hit_a_cluster = False

for i in range(len(number_string)):
    digit = number_string[i]
    if digit == prev_digit:
        if not hit_a_cluster:
            hit_a_cluster = True
            round_pos_i = i - 1
        counter += 1
    else:
        counter = 0
        hit_a_cluster = False
        prev_digit = digit
    if counter >= MAX_REPS:
        round_pos = round_pos_i

print(magnitude, round_pos)
