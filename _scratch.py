def re_based_decimal_fixer_zero(input_number_string):
    """Converts fractions like 6.25000007 (4 zeros ore above) to
    the normal, not that overly precise form like 6.25
    * Takes and returns a string."""
    import re
    result = False
    z0 = re.search('[1-9]+\\.(000)+0*[1-9]*', input_number_string)
    if z0:
        result = str(round(float(input_number_string)))

    if not result:
        for i in range(1, len(input_number_string) + 1):
            str_i = input_number_string[:i]
            z1 = re.search('\\.[1-9]+(000)', str_i)
            if z1:
                result = str_i[:-3]
                break

    if not result:
        for i in range(1, len(input_number_string) + 1):
            str_i = input_number_string[:i]
            z2 = re.search('\\.[1-9]*0+[1-9]+0+', str_i)
            if z2:
                result = str_i[:-1]
                break

    if not result:
        result = input_number_string

    return result


def e_remover(value, string_output=True):
    if 'e' in str(value):
        value = "{:.16f}".format(value)
        fixed = False
        while not fixed:
            if value[-1] == '0':
                value = value[:-1]
            else:
                fixed = True
    if not float(value) % 1:
        value = int(float(value))
    if string_output:
        value = str(value)
    return value


def auto_round(number, ignore_zeros=True, string_output=True):
    """accepts strings like 0.369999999997654, returns adequate versions"""
    MAX_REPS = 4
    number = float(number)


    class NotInRangeError(Exception):
        """the value is not supported (too large or too small)"""

        def __init__(self, message= 'the value has to be between 10**-13 and 10**13'):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return self.message

    if not 10**-14 < number < 10**14:
        raise NotInRangeError

    # magnitude = None
    # for power in range(-13, 14):
    #     if 10**power > number:
    #         magnitude = power - 1
    #         break

    number_string = str(number)

    prev_digit = ''
    counter = 1
    round_pos = None
    hit_a_cluster = False
    point_pos = len(number_string)

    if ignore_zeros:
        def zero_condition(x):
            return x != '0'
    else:
        def zero_condition(x):
            return True

    for i in range(len(number_string)):
        digit = number_string[i]
        if digit == '.':
            point_pos = i
        if digit == prev_digit and zero_condition(digit):
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
    else:
        result = number

    if not result % 1:
        result = int(result)

    if string_output:
        result = str(result)

    return result


fixer = re_based_decimal_fixer_zero
print(auto_round(78.000000))