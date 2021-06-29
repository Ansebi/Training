def auto_round(number):
    """accepts floats  like 0.369999999997654, returns adequate versions"""
    MAX_REPS = 4
    number = float(number)


    class NotInRangeError(Exception):
        """the value is not supported (too large or too small)"""

        def __init__(self, message= 'the value has to be between 10**-13 and 10**13'):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return self.message

    if not 10**-13 < number < 10**13:
        raise NotInRangeError

    magnitude = None
    for power in range(-13, 14):
        if 10**power > number:
            magnitude = power - 1
            break

    number_string = str(number)

    prev_digit = ''
    counter = 1
    round_pos = None
    hit_a_cluster = False
    point_pos = len(number_string)

    for i in range(len(number_string)):
        digit = number_string[i]
        if digit == '.':
            point_pos = i
        if digit == prev_digit:
            if not hit_a_cluster:
                hit_a_cluster = True
                round_pos_i = i - 1
            counter += 1
        else:
            if digit != '.':
                counter = 1
                hit_a_cluster = False
                prev_digit = digit
        if counter >= MAX_REPS:
            round_pos = round_pos_i

    if round_pos:
        result = round(number, round_pos - point_pos)
        if not result % 1:
            result = int(result)
    else:
        result = number

    return result

n = 77.000222222222
print(auto_round(n))
