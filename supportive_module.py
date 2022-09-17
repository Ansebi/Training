def factorize(n: int) -> list:
    """generate proper multiples to form a number for further factorization"""
    results = []
    i = 0
    divisor = 2
    while abs(n) > 1:
        if n % divisor == 0:
            results.append(divisor)
            n = n / divisor
            divisor = 2
        else:
            divisor += 1
    return results


def crossout(a, b):
    if a == b:
        a, b = [1], [1]
    else:
        a_count = 0
        while a_count in range(len(a)):
            switch = 0
            b_count = 0
            while b_count in range(len(b)):
                if b[b_count] == a[a_count]:
                    del b[b_count]
                    b_count = len(b) + 1
                    del a[a_count]
                    switch = 1
                else:
                    b_count += 1
            if switch == 0:
                a_count += 1
            if not a:
                a = [1]
            if not b:
                b = [1]
    c = 1
    for i in a:
        c = c * i
    a = c
    c = 1
    for i in b:
        c = c * i
    b = c
    return a, b


def fraction_simplifier(numerator, denominator):
    top, bottom = crossout(factorize(numerator), factorize(denominator))
    if bottom == 1:
        return str(top)
    else:
        return f'{top}/{bottom}'


def quadratics_composer():
    total_set = []
    counter = 0
    for a in range(-10, 10):
        for b in range(-13, 13):
            for c in range(-100, 100):
                D = b ** 2 - 4 * a * c
                if D >= 0:
                    r2D = D ** 0.5
                    try:
                        x1 = (-b + r2D) / (2 * a)
                    except:
                        pass
                    if x1 % 1 == 0:
                        try:
                            x2 = (-b - r2D) / (2 * a)
                        except:
                            pass
                        if x2 % 1 == 0:
                            counter += 1
                            particular_set = []
                            particular_set.append(a)
                            particular_set.append(b)
                            particular_set.append(c)
                            particular_set.append(int(x1))
                            particular_set.append(int(x2))
                            total_set.append(particular_set)

    return total_set


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
        value = "{:.16f}".format(float(value))
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


def auto_round(number, ignore_zeros=True, string_output=True, restrict=False):
    """accepts strings like 0.369999999997654, returns adequate versions"""
    MAX_REPS = 4
    #number = float(number)


    class NotInRangeError(Exception):
        """the value is not supported (too large or too small)"""

        def __init__(self, message= 'the value has to be between 10**-14 and 10**14'):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return self.message

    if restrict:
        if not 10**-14 < float(number) < 10**14:
            raise NotInRangeError

    # magnitude = None
    # for power in range(-13, 14):
    #     if 10**power > number:
    #         magnitude = power - 1
    #         break

    number_string = str(number)

    prev_digit = ''
    counter = 1
    round_pos = len(number_string)
    round_pos_change = False
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
            round_pos_change = True
    if round_pos_change:
        result = round(float(number), round_pos - point_pos)
    else:
        result = number

    if round(float(result), 0) == float(result):
        result = round(float(number), round_pos - point_pos)

    if string_output:
        result = str(result)

    return result
