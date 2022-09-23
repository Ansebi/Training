import random
from random import randint
import numpy as np
import supportive_module
from supportive_module import crossout
from supportive_module import factorize
from supportive_module import fraction_simplifier
from supportive_module import num_to_str


def test(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    right_answer = "test"
    right_answers = [right_answer]
    input_message = "test: "
    return right_answers, input_message, prompt


def add_negatives(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n = random.randint(10, 100)
    if random.randint(0, 1) == 1:
        n_sign = -1
    else:
        n_sign = 1

    m = random.randint(10, 100)
    if random.randint(0, 1) == 1:
        m_sign = -1
    else:
        m_sign = 1

    right_answer = n * n_sign + m * m_sign
    right_answer = str(right_answer)
    right_answers = [right_answer]
    input_message = str(n * n_sign) + "+" + str(m * m_sign) + " = " if m_sign == 1 else str(n * n_sign) + str(
        m * m_sign) + " = "

    return right_answers, input_message, prompt


def round_whole_numbers(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n = random.randint(1, 1000000)
    if random.randint(0, 1) == 1:
        n_sign = -1
    else:
        n_sign = 1

    m = 10 ** random.randint(1, 5)
    right_answer = n_sign * int(round(n / m, 0) * m)
    right_answer = str(right_answer)
    right_answers = [right_answer]
    input_message = str(n * n_sign) + " rounded by " + str(m) + " = "

    return right_answers, input_message, prompt


def round_decimals(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n = round(random.uniform(-1000, 1000), random.randint(5, 7))
    dp = random.randint(0, 4)
    right_answer = round(n, dp)
    if not dp:
        right_answer = int(right_answer)
    right_answer = str(right_answer)
    right_answers = [right_answer]
    input_message = str(n) + " rounded by " + str(10 ** (-dp)) + "(" + str(dp) + " d.p.) = "

    return right_answers, input_message, prompt


def multiply_decimals(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n = random.randint(0, 100)
    if random.randint(0, 1) == 1:
        n_sign = -1
    else:
        n_sign = 1

    m = round(random.randint(0, 12) * 10 ** random.randint(-3, 0), 4)
    right_answer = round(n_sign * n * m, 4)
    right_answers = [str(right_answer)]
    input_message = str(n * n_sign) + " * " + str(m) + " = "

    return right_answers, input_message, prompt


def multiplication_table(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    # n*m
    n = random.randint(1, 11)
    m = random.randint(1, 11)
    right_answer = n * m
    right_answers = [str(right_answer)]
    input_message = str(n) + " * " + str(m) + " = "
    return right_answers, input_message, prompt


def multiply_two_digits(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    # n*m
    n = random.randint(10, 100)
    m = random.randint(2, 11)
    right_answer = n * m
    right_answers = [str(right_answer)]
    input_message = str(n) + " * " + str(m) + " = "
    return right_answers, input_message, prompt


def multiply_hundreds(difficulty: int):
    # 26.05.2018 edition
    right_answers, input_message, prompt = None, None, None

    m, n = 1, 1
    if random.choice([0, 0, 1, 1, 1]) == 0:
        n = random.randint(0, 13) * 10 ** random.randint(0, 4)
        m = random.randint(1, 13) * 10 ** random.randint(0, 4)
    else:
        while m * n % 10 != 0:
            n = random.choice([random.randint(2, 9), random.randint(11, 13)])
            m = random.choice([random.randint(2, 9), random.randint(11, 13)])
    n = n * 10 ** random.randint(0, 4)
    m = m * 10 ** random.randint(0, 4)
    n_sign = random.choice([-1, 1])
    m_sign = random.choice([-1, 1])

    right_answer = n_sign * n * m_sign * m
    right_answers = [str(right_answer)]
    input_message = str(n * n_sign) + " * " + str(m) + " = " if m_sign == 1 else str(n * n_sign) + " * (" + str(
        m * m_sign) + ") = "
    return right_answers, input_message, prompt


def find_sum(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    input_message = ""
    right_answer = 0

    n, n_quantity, input_message_raw = [], [], []
    for i in range(3):
        n.append(random.randint(-50, 50))
        n_quantity.append(random.randint(0, 6))
        right_answer += n[i] * n_quantity[i]
        for counter in range(n_quantity[i]):
            input_message_raw.append(n[i])
        random.shuffle(input_message_raw)
    for counter in range(len(input_message_raw)):
        input_message += str(" " + str(input_message_raw[counter]) + " ")
    input_message = "sum(" + input_message + ")= "
    right_answers = [str(right_answer)]
    return right_answers, input_message, prompt


def powers(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # constants:
    low, high, mode, how_narrow_is_option_2, option_2_probability = 0, 15, 2, 3, 70

    option_1 = int(round(random.triangular(low, high, mode), 0))

    option_2 = int(round(
        random.triangular(
            mode - (mode - low) / how_narrow_is_option_2,
            mode + (high - mode) / how_narrow_is_option_2,
            mode),
        0))

    if random.randint(1, 100) > option_2_probability:
        n = option_1
    else:
        n = option_2
    # adjusting the power according to the base, excluding 0**0
    if n != 0:
        m = random.randint(0, 9 - n) if n < 8 else random.randint(0, 2)
    else:
        m = random.randint(1, 9 - n) if n < 8 else random.randint(1, 2)
    # adjusting the power according to the base, excluding 0**0 end
    right_answer = str(n ** m)
    right_answers = [right_answer]
    input_message = str(str(n) + " to the power of " + str(m) + " = ")
    return right_answers, input_message, prompt


def factorization(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    prime_numbers_up_to_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97]

    n_1 = random.choice(prime_numbers_up_to_100[0:3])
    if random.randint(0, 1):
        n_2 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_2 = 1
    if random.randint(0, 1):
        n_3 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_3 = 1
    if random.randint(0, 1):
        n_4 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_4 = 1
    if random.randint(0, 1):
        n_5 = random.choice(prime_numbers_up_to_100[0:4])
    else:
        n_5 = 1
    if random.randint(0, 1):
        n_6 = random.choice(prime_numbers_up_to_100[0:6])
    else:
        n_6 = 1
    # finish generating proper muliples to form a number for further factorization

    n = n_1 * n_2 * n_3 * n_4 * n_5 * n_6

    factorize(n)

    # converting factorization results:
    counter = 0
    for i in factorization.results:
        factorization.results[counter] = str(factorization.results[counter])
        counter += 1
    factorization.results = "*".join(factorization.results)
    # finish converting factorization results

    right_answer = factorization.results
    right_answers = [right_answer]
    input_message = str("factorize " + str(n) + ":  " + str(n) + " = ")

    return right_answers, input_message, prompt


def linear_equations(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    # ax+b=c
    a = random.randint(1, 9)
    a_sign = 1 if random.randint(0, 1) > 0 else -1
    a = a * a_sign

    right_answer = random.randint(0, 11)
    right_answer_sign = 1 if random.randint(0, 1) > 0 else -1
    right_answer = right_answer * right_answer_sign

    b = int(round(random.triangular(-50, 50, 0), 0))

    c = a * right_answer + b

    if a == 1:
        a_input_message = ""
    elif a == -1:
        a_input_message = "-"
    else:
        a_input_message = str(a)

    if b != 0:
        b_input_message = "+" + str(b) if b > 0 else str(b)
    else:
        b_input_message = ""

    input_message = a_input_message + "x" + b_input_message + "=" + str(c) + "\nx = "
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def linear_equations_lvl_2(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    # ax/d+b=c
    right_answer = 0.1
    while right_answer % 1 != 0:
        a = random.randint(1, 10) * random.choice([-1, 1])
        b = int(round(random.triangular(-50, 50, 0), 0))
        c = b + random.randint(-13, 13)
        d = random.randint(1, 13) * random.choice([-1, 1])
        right_answer = d * (c - b) / a
    right_answer = str(int(right_answer))

    if a == 1:
        a_input_message = ""
    elif a == -1:
        a_input_message = "-"
    else:
        a_input_message = str(a)

    if b != 0:
        b_input_message = "+" + str(b) if b > 0 else str(b)
    else:
        b_input_message = ""

    input_message = a_input_message + "x/" + str(d) + b_input_message + "=" + str(c) + "\nx = "
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def systems_easy(difficulty: int):
    """
    ax + by = n1
    cy + dz = n2
    ez + fx = n3
    """
    right_answers, input_message, prompt = None, None, None

    a, b, c, d, e, f, x, y, z = np.random.randint(1, 11, 9) * np.random.choice([-1, 1], 9)

    n1 = a * x + b * y
    n2 = c * y + d * z
    n3 = e * z + f * x

    line1 = f'{a}x {num_to_str(b)}y = {n1}'
    line2 = f'{c}y {num_to_str(d)}z = {n2}'
    line3 = f'{e}z {num_to_str(f)}x = {n3}'

    input_message = '\n'.join([line1, line2, line3]) + '\n'
    prompt = 'Find x y z. Response Example: 5 -5 10'
    right_answers = [f'{x} {y} {z}', f'{x}, {y}, {z}', f' {x} {y} {z}', f' {x} {y} {z} ']

    return right_answers, input_message, prompt


def division_remainders(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    divisor = random.randint(1, 11)
    remainder = random.randint(0, divisor - 1)
    quotient = random.randint(0, 9)
    divident = divisor * quotient + remainder
    if remainder > 0:
        if quotient != 0:
            right_answer = str(quotient) + "r" + str(remainder)
        else:
            right_answer = "0r" + str(remainder)
    else:
        if quotient != 0:
            right_answer = str(quotient)
        else:
            right_answer = str(0)

    input_message = str(divident) + ":" + str(divisor) + " = "
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def fraction_reduction(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    common_factor = random.randint(1, 11)
    n_1 = random.randint(1, 13)
    n_2 = random.randint(1, 13)
    if not n_1 % n_2:
        right_answer = int(n_1 / n_2)
    else:
        numerator = n_1 * common_factor
        denominator = n_2 * common_factor
        right_answer = fraction_simplifier(numerator, denominator)
    input_message = str(n_1 * common_factor) + "/" + str(n_2 * common_factor) + "= "
    right_answers = [right_answer]
    return right_answers, input_message, prompt


def fractions_to_decimals(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # generating numerator
    switch = random.randint(0, 2)
    if switch == 0:
        numerator = random.randint(1, 9)
    elif switch == 1:
        numerator = random.randint(1, 1000)
    else:
        numerator = random.randint(1, 100)
    # end generating numerator

    # generating denominator
    if random.randint(0, 2) == 0:
        denominator = 10 ** int(round(random.triangular(1, 6, 2), 0))
    else:
        denominator = 100
    # end generating denominator

    right_answer = numerator / denominator
    right_answers = [right_answer]
    input_message = "convert to decimals:" + str(numerator) + "/" + str(denominator) + "= "

    return right_answers, input_message, prompt


def add_decimals_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    if random.randint(1, 5) > 2:
        n = random.randint(0, 10)
    else:
        n = random.randint(10, 100) / 10
    n_sign = -1 if random.randint(1, 10) > 4 else 1

    if random.randint(1, 3) == 1 and n % 1 != 0:
        m = random.randint(0, 10)
    else:
        m = random.randint(10, 100) / 10
    m_sign = -1 if random.randint(1, 10) > 3 else 1

    n = n * n_sign
    m = m * m_sign

    right_answer = round(n + m, 2)

    if n % 1 == 0:
        n = int(n)
    if m % 1 == 0:
        m = int(m)

    if m >= 0:
        m_string = '+' + str(m)
    else:
        m_string = str(m)

    input_message = str(n) + m_string + " = "

    if right_answer % 1 == 0:
        right_answer = int(right_answer)
    right_answer = str(right_answer)
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def percent_of(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    switch = random.randint(1, 7)
    if switch <= 4:
        n = 10 * random.randint(20, 100)
        percent = random.randint(1, 20) * 5
        right_answer = n * percent / 100
    elif switch == 5:
        n = random.randint(1, 100)
        percent = random.randint(1, 60) * 10
        right_answer = n * percent / 100
    elif switch == 6:
        right_answer = 0.1
        while right_answer % 1 != 0:
            n = random.randint(1, 600)
            percent = random.randint(0, 100)
            right_answer = n * percent / 100
    else:
        right_answer = 0.1
        percent = 100
        while right_answer % 1 != 0 or percent == 100:
            n = random.randint(1, 600)
            percent = random.randint(0, 600)
            right_answer = n * percent / 100

    input_message = str(percent) + "% of " + str(n) + " = "
    if right_answer % 1 == 0:
        right_answer = int(right_answer)
    right_answer = str(right_answer)
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def percent_of_no_calculation(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    switch = random.randint(1, 5)
    # print("switch =",switch)
    if switch <= 4:
        n = 10 * random.randint(20, 100)
        percent = random.randint(1, 20) * 5

    elif switch == 5:
        n = random.randint(1, 100)
        percent = random.randint(1, 60) * 10

    elif switch == 6:
        n = random.randint(1, 600)
        percent = random.randint(0, 100)

    else:
        n = random.randint(1, 600)
        percent = random.randint(0, 600)

    coeff = percent / 100
    if coeff % 1 == 0:
        coeff = int(coeff)
    coeff = str(coeff)

    right_answer = str(n) + "*" + coeff
    right_answers = [right_answer]
    input_message = str(percent) + "% of " + str(n) + " = "

    return right_answers, input_message, prompt


def percent_change(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    switch = random.randint(1, 7)
    if switch <= 4:
        n = random.randint(1, 100) * 10 ** random.randint(0, 2)
        percent = random.randint(1, 20) * 5
        percent_delta = n * percent / 100
    elif switch == 5:
        percent_delta = 0.1
        while percent_delta % 1 != 0:
            n = random.randint(1, 600)
            percent = random.randint(0, 100)
            percent_delta = n * percent / 100
    # the following two are up to 600%
    elif switch == 6:
        n = random.randint(1, 100)
        percent = random.randint(1, 60) * 10
        percent_delta = n * percent / 100
    else:
        percent_delta = 0.1
        percent = 100
        while percent_delta % 1 != 0 or percent == 100:
            n = random.randint(1, 600)
            percent = random.randint(0, 600)
            percent_delta = n * percent / 100
    # end(the following two are up to 600%)

    if random.randint(0, 4) <= 3 and switch <= 5:
        percent_delta_sign = -1
        crease = "Decrease "
    else:
        percent_delta_sign = 1
        crease = "Increase "

    right_answer = n + percent_delta * percent_delta_sign
    right_answers = [right_answer]
    input_message = "It was " + str(n) + "." + crease + str(percent) + "%. Now it equals "
    x = float(input(input_message))
    return right_answers, input_message, prompt


def roots(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # constants:
    low, high, mode, how_narrow_is_option_2, option_2_probability = 0, 17, 2, 3, 40

    option_1 = int(round(random.triangular(low, high, mode), 0))

    option_2 = int(round(
        random.triangular(5, 20, 11), 0))

    if random.randint(1, 100) > option_2_probability:
        right_answer = option_1
    else:
        right_answer = option_2

    # proper powers
    if right_answer == 2:
        power = random.randint(2, 14)
    elif right_answer < 6:
        power = random.randint(2, 9 - right_answer)
    elif right_answer < 9:
        power = random.randint(2, 3)
    else:
        power = 2
    # end(proper powers)

    n = right_answer ** power

    if power == 2:
        degree_of_the_root = "square"
    elif power == 3:
        degree_of_the_root = "cubic"
    else:
        degree_of_the_root = str(power) + "th"

    input_message = str(degree_of_the_root + " root of " + str(n) + " = ")
    right_answers = [right_answer]
    x = int(input(input_message))
    return right_answers, input_message, prompt


def logs(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    mode = random.randint(1, 3)
    base = random.randint(2, 13)
    if mode < 3:
        # proper powers
        if base == 2:
            power = random.randint(0, 14)
        elif base < 6:
            power = random.randint(0, 9 - base)
        elif base < 9:
            power = random.randint(0, 3)
        else:
            power = random.randint(0, 2)
        # end(proper powers)
    else:
        if base == 2:
            power = random.randint(1, 14)
        elif base < 6:
            power = random.randint(1, 9 - base)
        elif base < 9:
            power = random.randint(1, 3)
        else:
            power = random.randint(1, 2)

    number = base ** power

    if mode == 1:
        # log a (b) = x
        right_answer = power
        input_message = "log " + str(base) + " (" + str(number) + ") = "
    elif mode == 2:
        # log a (x) = c
        right_answer = number
        input_message = "log " + str(base) + " (x) = " + str(power) + "\nx = "
    else:
        # log x (b) = c
        right_answer = base
        input_message = "log x (" + str(number) + ") = " + str(power) + "\nx = "

    right_answer = str(right_answer)
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def adding_fractions_easy(difficulty: int):
    import supportive_module
    right_answers, input_message, prompt = None, None, None

    # a/b+c/d

    a = random.randint(1, 13)
    b = random.randint(1, 13)
    switch = random.randint(0, 2)
    if switch == 0:
        c = random.randint(1, 13)
        d = random.randint(1, 13)
    elif switch == 1:
        c = random.choice([random.randint(1, 5), random.randint(1, 13)])
        d = random.randint(1, 5) * b
    elif switch == 2:
        c = random.randint(1, 13)
        d = random.randint(1, 13) * b

    if random.randint(0, 1) == 0:
        a, b, c, d = c, d, a, b

    # off ab_sign=random.choice[-1,1]
    # off cd_sign=random.choice[-1,1]

    # (a*d+c*b)/(b*d)
    numerator = a * d + c * b
    denominator = b * d

    fraction_simplifier = supportive_module.fraction_simplifier
    crossout = supportive_module.crossout

    fraction_simplifier(numerator, denominator)

    if crossout.top < crossout.bottom or crossout.bottom == 1:
        right_answer = fraction_simplifier.output
    else:
        whole = crossout.top // crossout.bottom
        fraction_top = crossout.top % crossout.bottom
        right_answer = str(whole) + " " + str(fraction_top) + "/" + str(crossout.bottom)

    input_message = str(a) + "/" + str(b) + " + " + str(c) + "/" + str(d) + " = "
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def division_mixed_fractions_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # composing apropriate numbers
    n1 = random.choice([1, random.choice([2, 3, 5])])
    n2 = random.choice([1, 10, random.choice([2, 3, 5])])
    n3 = random.choice([1, 1, 1, random.choice([2, 3, 5, 7, 11])])
    n4 = random.choice([2, 3, 5, 7, 11, 13])
    divident = n1 * n2 * n3 * n4

    n2 = random.choice([1, random.choice([2, 3, 5])])
    n3 = random.choice([1, 1, random.choice([2, 3, 5, 7, 11])])
    n4 = random.choice([2, 3, 5, 7, 11, 13])
    divisor = n2 * n3 * n4

    top, bottom = crossout(factorize(divident), factorize(divisor))
    fraction_reduced = fraction_simplifier(top, bottom)

    # converting fraction to a mixed number
    if top < bottom or bottom == 1:
        right_answer = fraction_reduced
    else:
        whole = top // bottom
        fraction_top = top % bottom
        right_answer = f'{whole} {fraction_top}/{bottom}'
    # end converting fraction to a mixed number
    input_message = f'{divident}/{divisor} = '
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def division_mixed_fractions(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # composing appropriate numbers
    divident = random.choice(
        [random.randint(80, 160),
         random.randint(80, 480),
         random.randint(80, 800)]
    )
    divisor = divident // random.randint(1, 10)

    top, bottom = crossout(factorize(divident), factorize(divisor))
    fraction_reduced = fraction_simplifier(top, bottom)

    # converting fraction to a mixed number
    if top < bottom or bottom == 1:
        right_answer = fraction_reduced
    else:
        whole = top // bottom
        fraction_top = top % bottom
        right_answer = f'{whole} {fraction_top}/{bottom}'
    # end converting fraction to a mixed number
    input_message = f'{divident}/{divisor} = '
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def compare_two_numbers_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    option1 = round(random.randint(-1000, 1000) * 10 ** random.randint(-4, 4), 6)
    option2 = round(random.randint(-100, 100) * 10 ** random.randint(-4, 3), 6)
    n1 = random.choice([option1, option2])
    option1 = round(random.randint(-1000, 1000) * 10 ** random.randint(-4, 4), 6)
    option2 = round(random.randint(-100, 100) * 10 ** random.randint(-4, 3), 6)
    n2 = random.choice([option1, option2])

    if n1 < n2:
        right_answer = "<"
    elif n1 > n2:
        right_answer = ">"
    else:
        right_answer = "="
    print(str(n1) + " ... " + str(n2) + "\n")
    input_message = str(n1) + " "
    right_answers = [right_answer]

    print(str(n2))
    return right_answers, input_message, prompt


def multilply_two_digits(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    if random.randint(0, 1) == 1:
        n1 = random.randint(3, 13)
        n2 = random.randint(3, 13)
    else:
        n1 = int(round(random.triangular(1, 99, 25), 0))
        n2 = random.randint(0, 10)

    right_answer = str(n1 * n2)
    right_answers = [right_answer]
    input_message = str(n1) + " * " + str(n2) + " = "

    return right_answers, input_message, prompt


def factorizing_square_of_sum(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    alphabet_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                      'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'q', 'r', 's', 't', 'u', 'v',
                      'w', 'x', 'y', 'z']
    switch = 'NOT OKAY'

    n1 = random.randint(1, 13)
    n1_string = str(n1) if n1 != 1 else ""
    n1_square_string = str(n1 ** 2) if n1 != 1 else ""
    n2 = random.randint(1, 13)
    n2_string = str(n2) if n2 != 1 else ""
    n2_square_string = str(n2 ** 2) if n2 != 1 else ""

    the_sign = random.choice(['+', '-'])

    while switch == 'NOT OKAY':
        letter1 = random.choice([alphabet_small.pop(random.randint(0, len(alphabet_small) - 1)), ""])
        letter1_power = '2' if letter1 != "" else ""
        letter2 = random.choice([alphabet_small.pop(random.randint(0, len(alphabet_small) - 1)), ""])
        letter2_power = '2' if letter2 != "" else ""
        switch = 'OKAY, GO' if letter1 != letter2 and letter1 != n1_string and letter2 != n2_string else 'NOT OKAY'

    right_answer = '(' + n1_string + letter1 + the_sign + n2_string + letter2 + ')2'
    input_message = (n1_square_string + letter1 + letter1_power +
                     the_sign +
                     str(2 * n1 * n2) + letter1 + letter2 +
                     '+' + n2_square_string + letter2 + letter2_power + ' = ')

    right_answers = [right_answer]

    return right_answers, input_message, prompt


def complete_square_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n1 = random.randint(1, 13)
    n1_string = str(n1) if n1 != 1 else ""
    n1_square_string = str(n1 ** 2) if n1 != 1 else ""
    n2 = random.randint(1, 13)

    the_sign = random.choice(['+', '-'])

    right_answer = '(' + n1_string + 'x' + the_sign + str(n2) + ')2'
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     str(2 * n1 * n2) + 'x' +
                     '+' + str(n2 ** 2) + ' = ')

    right_answers = [right_answer]

    return right_answers, input_message, prompt


def complete_square_a1(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    n1 = random.randint(1, 13)
    n1_string = str(n1) if n1 != 1 else ""
    n1_square_string = str(n1 ** 2) if n1 != 1 else ""
    n2 = random.randint(1, 13)

    the_sign = random.choice(['+', '-'])

    right_answer = '(' + n1_string + 'x' + the_sign + str(n2) + ')2'
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     str(2 * n1 * n2) + 'x' +
                     '+' + '...' + ' = ')

    right_answers = [right_answer]

    return right_answers, input_message, prompt


def complete_square_a2(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # (a+b)2=a2+2ab+b2

    n1 = random.randint(1, 13)
    n1_string = str(n1) if n1 != 1 else ""
    n1_square_string = str(n1 ** 2) if n1 != 1 else ""
    n2 = random.randint(1, 13)

    the_noise_v1 = 10 * randint(-10, 10)
    the_noise_v2 = randint(-20, 20)
    the_noise = random.choice([the_noise_v1, the_noise_v2])

    the_sign = random.choice(['+', '-'])

    b2 = n2 ** 2 + the_noise
    if b2 < 0:
        b2 = str(b2)
    elif b2 == 0:
        b2 = ''
    else:
        b2 = '+' + str(b2)

    if the_noise < 0:
        the_noise = str(the_noise)
    elif the_noise == 0:
        the_noise = ''
    else:
        the_noise = '+' + str(the_noise)

    right_answer = '(' + n1_string + 'x' + the_sign + str(n2) + ')2' + the_noise
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     str(2 * n1 * n2) + 'x' + b2 + ' = ')
    prompt = 'HINT: answer in the form of (a+b)2+n'
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def complete_square_a2_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    # (a+b)2=a2+2ab+b2

    n1 = random.randint(1, 13)
    n1_string = str(n1) if n1 != 1 else ""
    n1_square_string = str(n1 ** 2) if n1 != 1 else ""
    n2 = random.randint(1, 13)

    the_noise_v1 = 10 * randint(-10, 10)
    the_noise_v2 = randint(-20, 20)
    the_noise = random.choice([the_noise_v1, the_noise_v2])

    the_sign = random.choice(['+', '-'])

    b2 = n2 ** 2 + the_noise
    if b2 < 0:
        b2 = str(b2)
    elif b2 == 0:
        b2 = ''
    else:
        b2 = '+' + str(b2)

    if the_noise < 0:
        the_noise = str(the_noise)
    elif the_noise == 0:
        the_noise = ''
    else:
        the_noise = '+' + str(the_noise)

    right_answer = the_noise
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     str(2 * n1 * n2) + 'x' + b2 + ' = ')
    input_message += '(' + n1_string + 'x' + the_sign + str(n2) + ')2'
    prompt = 'HINT: answer in the form of (a+b)2+n'
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def complete_square_a3(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    the_multiplier = randint(2, 5)

    n2 = randint(1, 13)

    the_sign = random.choice(['+', '-'])

    right_answer = str(the_multiplier) + '(x' + the_sign + str(n2) + ')2'

    input_message = (str(the_multiplier) + 'x2' +
                     the_sign +
                     str(the_multiplier * 2 * n2) + 'x' +
                     '+' + str((n2 ** 2) * the_multiplier) + ' = ')

    right_answers = [right_answer]
    prompt = 'represent as: a(x+b)2'

    return right_answers, input_message, prompt


def complete_square_a4(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    the_multiplier = randint(2, 5)

    n2 = randint(1, 13)

    the_sign = random.choice(['+', '-'])

    right_answer = str(the_multiplier) + '(x' + the_sign + str(n2) + ')2'

    input_message = (str(the_multiplier) + 'x2' +
                     the_sign +
                     str(the_multiplier * 2 * n2) + 'x' +
                     '+' + '...' + ' = ')

    right_answers = [right_answer]
    prompt = 'represent as: a(x+b)2'

    return right_answers, input_message, prompt


def complete_square_a5(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    the_multiplier = randint(2, 5)

    n2 = randint(1, 13)

    the_noise_v1 = randint(-20, 20)
    the_noise_v2 = 10 * randint(-5, 5)
    the_noise = random.choice([the_noise_v1, the_noise_v2])
    if the_noise > 0:
        the_noise_string = '+' + str(the_noise)
    elif the_noise == 0:
        the_noise_string = ''
    else:
        the_noise_string = str(the_noise)

    the_sign = random.choice(['+', '-'])

    right_answer = str(the_multiplier) + '(x' + the_sign + str(n2) + ')2' + the_noise_string

    input_message = (str(the_multiplier) + 'x2' +
                     the_sign +
                     str(the_multiplier * 2 * n2) + 'x' +
                     '+' + str((n2 ** 2) * the_multiplier + the_noise) + ' = ')

    right_answers = [right_answer]

    prompt = 'represent as: a(x+b)2+c'

    return right_answers, input_message, prompt


def star_count_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    max_n = 9
    max_len = 20
    input_message = ' ' * (max_len + 1)
    while len(input_message) > max_len:
        n1 = random.randint(1, max_n)
        if n1 > 2:
            n2 = random.randint(2, (max_n - n1 + 3))
        else:
            n2 = random.randint(4, 9)
        n2 = 1 if n2 == 0 else n2
        product = n1 * n2
        if product < 4:
            n1, n2 = random.randint(5, 7), random.randint(3, 5)
            product = n1 * n2
        input_message = ('*' * n1 + '\n') * n2 + ' = '
    right_answer = str(product)
    right_answers = [right_answer]

    return right_answers, input_message, prompt


def estimate(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    total_n = randint(3, 8)
    max_species = 4
    bottom = 100
    ceiling = 800
    min_repeat = 1
    max_repeat = 5

    def g():  # it's a global costyl
        pass

    g.items_remaining = total_n
    g.question = ''
    g.estimate = 0

    def item_n(bottom, ceiling, max_repeat, i):
        locals()['item_' + str(i)] = randint(bottom, ceiling)
        item_i = locals()['item_' + str(i)]
        if g.items_remaining > 0:
            locals()['n_item_' + str(i)] = randint(min_repeat, g.items_remaining)
            n_item_i = locals()['n_item_' + str(i)]
            g.items_remaining -= n_item_i
        else:
            locals()['n_item_' + str(i)] = 0
            n_item_i = locals()['n_item_' + str(i)]

        g.question += ((str(item_i) + '   ') * n_item_i)
        the_order = 10 ** (len(str(item_i)) - 1)
        item_i_estimate = int(round(item_i / the_order, 0)) * the_order
        g.estimate += item_i_estimate * n_item_i

    for i in range(1, max_species + 1):
        item_n(bottom, ceiling, max_repeat, i)

    input_message = g.question + '\n' * 2
    right_answer = str(g.estimate)
    right_answers = [right_answer]
    prompt = 'Estimate the sum, 1 s.f. each:'

    return right_answers, input_message, prompt


def complex_roots(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    proper_condition = False
    while proper_condition == False:
        prime_option_1 = random.choice(primes_list[0:3])
        prime_option_2 = random.choice(primes_list)
        prime = random.choice([prime_option_1, prime_option_2])
        to_be_squarred = randint(2, 12)
        squarred = to_be_squarred ** 2
        input_message = squarred * prime
        if prime == prime_option_1:
            proper_condition = True
        if input_message < 200:
            proper_condition = True
        if input_message > 360:
            proper_condition = False

    input_message = 'r2(' + str(input_message) + ') = '
    right_answer = str(to_be_squarred)
    right_answer += 'r2(' + str(prime) + ')'
    right_answers = [right_answer]

    # prompt='type r2(x) of square root of x'
    return right_answers, input_message, prompt


def quadratic_equations_easy(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    import supportive_module
    quadratics_composer = supportive_module.quadratics_composer
    quadratics_composer()
    total_set = quadratics_composer.total_set
    the_particular_set = random.choice(total_set)

    a = the_particular_set[0]
    b = the_particular_set[1]
    c = the_particular_set[2]
    x1 = the_particular_set[3]
    x2 = the_particular_set[4]

    right_answer1 = str(x1) + ',' + str(x2)
    right_answer2 = str(x2) + ',' + str(x1)
    right_answers = [right_answer1, right_answer2]
    if x1 == x2:
        right_answers = [right_answer1, str(x1)]

    a = str(a)
    if a == '1':
        a = ''
    if a == '-1':
        a = '-'
    ax2 = a + 'x2'

    if b > 0:
        b_sign = '+'
    else:
        b_sign = ''
    b = str(b)
    bx = b + 'x'
    if b == '0':
        bx = ''
    if b == '1':
        bx = 'x'
    if b == '-1':
        bx = '-x'
    bx = b_sign + bx

    if c > 0:
        c_sign = '+'
    else:
        c_sign = ''
    c = str(c)
    if c == '0':
        c = ''
    c = c_sign + c

    input_message = ax2 + bx + c + '=0\n'

    return right_answers, input_message, prompt


def quadratic_equations_calculator(difficulty: int):
    right_answers, input_message, prompt = None, None, None

    a1 = randint(-10, -1)
    a2 = randint(1, 10)
    a = random.choice([a1, a2])
    b1 = randint(-10, -1)
    b2 = randint(1, 10)
    b = random.choice([b1, b2])
    c1 = randint(-10, -1)
    c2 = randint(1, 10)
    c = random.choice([c1, c2])
    D = b ** 2 - 4 * a * c
    if D < 0:
        right_answers = ['']
    elif D == 0:
        x = -b / (2 * a)
        x = round(x, 1)
        if x % 1 == 0:
            x = int(x)
        right_answers = [str(x)]
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x1 = round(x1, 1)
        if x1 % 1 == 0:
            x1 = int(x1)
        x2 = (-b - D ** 0.5) / (2 * a)
        x2 = round(x2, 1)
        if x2 % 1 == 0:
            x2 = int(x2)
        right_answer1 = str(x1) + ',' + str(x2)
        right_answer2 = str(x2) + ',' + str(x1)
        right_answers = [right_answer1, right_answer2]

    a = str(a)
    if a == '1':
        a = ''
    if a == '-1':
        a = '-'
    ax2 = a + 'x2'

    if b > 0:
        b_sign = '+'
    else:
        b_sign = ''
    b = str(b)
    bx = b + 'x'
    if b == '0':
        bx = ''
    if b == '1':
        bx = 'x'
    if b == '-1':
        bx = '-x'
    bx = b_sign + bx

    if c > 0:
        c_sign = '+'
    else:
        c_sign = ''
    c = str(c)
    if c == '0':
        c = ''
    c = c_sign + c

    prompt = 'give your answers rounded to 1d.p.'

    # input_message=prompt
    # input_message+='\n'
    input_message = ax2 + bx + c + '=0\n'
    return right_answers, input_message, prompt


def value_function_quadratic(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    x_v1 = randint(-9, 9)
    x_v2 = randint(-2, 0)
    x_v3 = randint(-5, -1)
    x_v4 = randint(-3, -1)
    x = random.choice([x_v1, x_v2, x_v3, x_v4])
    a1 = randint(-10, -1)
    a2 = randint(1, 10)
    a = random.choice([a1, a2])
    b1 = randint(-10, -1)
    b2 = randint(1, 10)
    b = random.choice([b1, b2])
    c1 = randint(-10, -1)
    c2 = randint(1, 10)
    c = random.choice([c1, c2])
    fx = a * (x ** 2) + b * x + c
    right_answers = [str(fx)]

    a = str(a)
    if a == '1':
        a = ''
    if a == '-1':
        a = '-'
    ax2 = a + 'x2'

    if b > 0:
        b_sign = '+'
    else:
        b_sign = ''
    b = str(b)
    bx = b + 'x'
    if b == '0':
        bx = ''
    if b == '1':
        bx = 'x'
    if b == '-1':
        bx = '-x'
    bx = b_sign + bx

    if c > 0:
        c_sign = '+'
    else:
        c_sign = ''
    c = str(c)
    if c == '0':
        c = ''
    c = c_sign + c

    prompt = 'find the value of the function:'

    # input_message=prompt
    # input_message+='\n'
    input_message = 'f(x)=' + ax2 + bx + c
    input_message += '\n'
    input_message += 'f(' + str(x) + ')='
    return right_answers, input_message, prompt


def factoring_quadratics(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    quadratics_composer = supportive_module.quadratics_composer
    x1 = 0
    x2 = 0
    a = 1
    while x1 == 0 or x2 == 0 or a == 1:
        quadratics_composer()
        total_set = quadratics_composer.total_set
        the_particular_set = random.choice(total_set)

        a = the_particular_set[0]
        b = the_particular_set[1]
        c = the_particular_set[2]
        x1 = the_particular_set[3]
        x2 = the_particular_set[4]

    x1 = -x1  # (x-x1) requires the opposite sign
    x2 = -x2  # (x-x2) requires the opposite sign
    if x1 < 0:
        str_x1 = str(x1)
    else:
        str_x1 = '+' + str(x1)
    if x2 < 0:
        str_x2 = str(x2)
    else:
        str_x2 = '+' + str(x2)

    a = str(a)
    if a == '1':
        a = ''
    if a == '-1':
        a = '-'
    ax2 = a + 'x2'

    if b > 0:
        b_sign = '+'
    else:
        b_sign = ''
    b = str(b)
    bx = b + 'x'
    if b == '0':
        bx = ''
    if b == '1':
        bx = 'x'
    if b == '-1':
        bx = '-x'
    bx = b_sign + bx

    if c > 0:
        c_sign = '+'
    else:
        c_sign = ''
    c = str(c)
    if c == '0':
        c = ''
    c = c_sign + c

    right_answer1 = a + '(x' + str_x1 + ')(x' + str_x2 + ')'
    right_answer2 = a + '(x' + str_x2 + ')(x' + str_x1 + ')'
    right_answers = [right_answer1, right_answer2]
    if x1 == x2:
        right_answers.append(a + '(x' + str_x1 + ')2')

    input_message = ax2 + bx + c + '='
    prompt = 'HINT: a(x-x1)(x-x2)'
    return right_answers, input_message, prompt


def convert_units(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    DELTA_RANGE = 10  # a power of 10 the range between the units to convert
    MAX_ZEROS = 7
    MAX_ZEROS_EASY = 5
    MAX_SIGNIFICANT_FIGURES = 100

    magnitudes = [0.000001, 0.000005,
                  0.00001, 0.00005,
                  0.0005, 0.005, 0.01, 0.5,
                  0.0001, 0.001, 0.01, 0.1,
                  1, 5, 10, 50, 100, 500,
                  1000, 5000, 10000, 50000]
    magnitudes_EASY = [0.005, 0.01, 0.5,
                       0.001, 0.01, 0.1,
                       1, 5, 10, 50, 100, 500,
                       1000, 5000]

    prefixes_dict = {'p': -12, 'n': -9, 'mc': -6, 'm': -3,
                     'c': -2, 'd': -1, 'u': 0,
                     'k': 3, 'M': 6, 'G': 9, 'T': 12}
    prefixes_dict_RUS = {'м': -3, 'c': -2, 'д': -1, 'u': 0, 'к': 3}

    units = ['g', 'm', 's', 'N', 'J', 'W', 'A', 'Hz']
    units_RUS = ['м']

    if not difficulty:
        units = units_RUS
        prefixes_dict = prefixes_dict_RUS
        magnitudes = magnitudes_EASY
        MAX_ZEROS = MAX_ZEROS_EASY

    prefixes = list(prefixes_dict.keys())
    prefixes.remove('u')

    unit = random.choice(units)

    n = random.randint(1, MAX_SIGNIFICANT_FIGURES)
    k = random.choice(magnitudes)

    value = n * k
    value = str(value)
    e_remover = supportive_module.e_remover
    value = e_remover(value)

    fixer = supportive_module.re_based_decimal_fixer_zero
    auto_round = supportive_module.auto_round
    value = e_remover(auto_round(fixer(value)))

    okay = False
    while not okay:
        prefix_1 = random.choice(prefixes)
        prefix_2 = random.choice(prefixes)
        if prefix_2 != prefix_1:
            delta = prefixes_dict[prefix_1] - prefixes_dict[prefix_2]
            if abs(delta) < DELTA_RANGE:
                right_answer = float(value) * 10 ** delta
                if '0' * MAX_ZEROS not in e_remover(right_answer):
                    okay = True

    right_answer = \
        e_remover(
            fixer(
                e_remover(
                    auto_round(
                        e_remover(
                            right_answer
                        )))))

    right_answers = [right_answer]
    if prefix_1 == 'u':
        prefix_1 = ''
    if prefix_2 == 'u':
        prefix_2 = ''

    prompt = 'Convert the following values to the new units:'
    input_message = str(value) + ' ' + prefix_1 + unit + ' = ... ' + prefix_2 + unit + '\n'
    return right_answers, input_message, prompt


def large_division(difficulty: int):
    right_answers, input_message, prompt = None, None, None
    # c = a * b
    ok = False
    while not ok:
        d = random.randint(1, difficulty + 1)
        a1 = random.choice([1, 1, 1, 5, 10, 100, 101, 1001])
        a2 = random.randint(1, 101)
        a3 = random.randint(1, 10)
        a = a1 * a2 * a3 * d
        b1 = random.randint(1, 100)
        b2 = random.choice([1, 1, 1, 5, 10, 100, 101])
        b = b1 * b2
        if 500 < a < 10000:
            if 90 < b < 1000:
                ok = True
    c = a * b
    prompt = 'Divide the following, the answer is a whole number:'
    input_message = f'{c} / {b} = ... \n'
    right_answers = [a]
    return right_answers, input_message, prompt


def open_close_brackets(difficulty: int):
    """
    forward: n(ax + by) = nax + nby
    backward: nax + nby = n(ax + by)
    """
    right_answers, input_message, prompt = None, None, None
    alphabet = 'abcdefghijkmnpqrstuvwxyz'
    d = abs(difficulty)
    mode = random.choice(['forward', 'backward'])
    x, y = np.random.choice(list(alphabet), 2, replace=False)
    if mode == 'forward':
        okay = False
        while not okay:
            a, b, n = np.random.randint(1, 6 + d, 3) * np.random.choice([-1, 1], 3)
            conditions = [abs(a) != abs(b), abs(n) != 1]
            okay = True if all(conditions) else False
    else:
        primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        a, b = np.random.choice(primes[:max([d, 6])], 2, replace=False) * np.random.choice([-1, 1], 2)
        n = random.randint(2, 12) * random.choice([-1, 1])
    na = num_to_str(n * a, in_middle=False, remove_one=True)
    nb = num_to_str(n * b, remove_one=True)
    a = num_to_str(a, in_middle=False, remove_one=True)
    b = num_to_str(b, remove_one=True)
    n_str = num_to_str(n, in_middle=False, remove_one=True)
    state0 = f"{n_str}({a}{x} {b}{y})"
    state1 = f"{na}{x} {nb}{y}"
    prompt = 'Open the brackets. Example: 5(x + 2y) = 5x + 10y'
    if mode == 'backward':
        state0, state1 = state1, state0
        factor_sign = 'NEGATIVE (-)' if n < 0 else 'POSITIVE (+)'
        prompt = 'Factorize the following. Example: 5x + 10y = 5(x + 2y)'
        prompt += f'\nThe factor is {factor_sign}'
    input_message = f"{state0} = "
    right_answers = [state1]

    return right_answers, input_message, prompt


exercises_dictionary = {
    "Test": {
        'function': test,
        'default_difficulty': 0},
    "Add negatives": {
        'function': add_negatives,
        'default_difficulty': 0},
    "Round whole numbers": {
        'function': round_whole_numbers,
        'default_difficulty': 0},
    "Round decimals": {
        'function': round_decimals,
        'default_difficulty': 0},
    "Multiply decimals": {
        'function': multiply_decimals,
        'default_difficulty': 0},
    "Multiply hundreds": {
        'function': multiply_hundreds,
        'default_difficulty': 0},
    "Find sum": {
        'function': find_sum,
        'default_difficulty': 0},
    "Powers": {
        'function': powers,
        'default_difficulty': 0},
    "Factorization": {
        'function': factorization,
        'default_difficulty': 0},
    "Linear equations": {
        'function': linear_equations,
        'default_difficulty': 0},
    "Linear equations: level 2": {
        'function': linear_equations_lvl_2,
        'default_difficulty': 0},
    "Systems (easy)": {
        'function': systems_easy,
        'default_difficulty': 0},
    "Division: remainders": {
        'function': division_remainders,
        'default_difficulty': 0},
    "Fraction reduction": {
        'function': fraction_reduction,
        'default_difficulty': 0},
    "Fractions to decimals": {
        'function': fractions_to_decimals,
        'default_difficulty': 0},
    "Add decimals (easy)": {
        'function': add_decimals_easy,
        'default_difficulty': 0},
    "Percent of": {
        'function': percent_of,
        'default_difficulty': 0},
    "Percent of (no calculation)": {
        'function': percent_of_no_calculation,
        'default_difficulty': 0},
    "Percent change": {
        'function': percent_change,
        'default_difficulty': 0},
    "Roots": {
        'function': roots,
        'default_difficulty': 0},
    "Logs": {
        'function': logs,
        'default_difficulty': 0},
    "Adding fractions (easy)": {
        'function': adding_fractions_easy,
        'default_difficulty': 0},
    "Division: mixed fractions (easy)": {
        'function': division_mixed_fractions_easy,
        'default_difficulty': 0},
    "Division: mixed fractions": {
        'function': division_mixed_fractions,
        'default_difficulty': 0},
    "Compare two numbers (easy)": {
        'function': compare_two_numbers_easy,
        'default_difficulty': 0},
    "Multiply two digits": {
        'function': multilply_two_digits,
        'default_difficulty': 0},
    "Factorizing square of sum": {
        'function': factorizing_square_of_sum,
        'default_difficulty': 0},
    "Complete square (easy)": {
        'function': complete_square_easy,
        'default_difficulty': 0},
    "Complete square A1": {
        'function': complete_square_a1,
        'default_difficulty': 0},
    "Complete square A2 (easy)": {
        'function': complete_square_a2_easy,
        'default_difficulty': 0},
    "Complete square A2": {
        'function': complete_square_a2,
        'default_difficulty': 0},
    "Complete square A3": {
        'function': complete_square_a3,
        'default_difficulty': 0},
    "Complete square A4": {
        'function': complete_square_a4,
        'default_difficulty': 0},
    "Complete square A5": {
        'function': complete_square_a5,
        'default_difficulty': 0},
    "Star count (easy)": {
        'function': star_count_easy,
        'default_difficulty': 0},
    "Estimate sum": {
        'function': estimate,
        'default_difficulty': 0},
    "Complex roots": {
        'function': complex_roots,
        'default_difficulty': 0},
    "Quadratic equations (easy)": {
        'function': quadratic_equations_easy,
        'default_difficulty': 0},
    "Quadratic equations (calculator)": {
        'function': quadratic_equations_calculator,
        'default_difficulty': 0},
    "Value of function: Quadratic": {
        'function': value_function_quadratic,
        'default_difficulty': 0},
    "Factoring Quadratics": {
        'function': factoring_quadratics,
        'default_difficulty': 0},
    "Multiply Two Digits": {
        'function': multiply_two_digits,
        'default_difficulty': 0},
    "Multiplication Table": {
        'function': multiplication_table,
        'default_difficulty': 0},
    "Convert Units": {
        'function': convert_units,
        'default_difficulty': 0},
    "Large Division": {
        'function': large_division,
        'default_difficulty': 0},
    "Open brackets | Close brackets": {
        'function': open_close_brackets,
        'default_difficulty': 6}
}
