import random
from random import randint

def test():
    global ans, right_answers, input_message
    right_answer = "test"
    right_answers = [right_answer]
    input_message = "test: "
    # ans=input(input_message)


def add_negatives():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def round_whole_numbers():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def round_decimals():
    global ans, right_answers, input_message

    n = round(random.uniform(-1000, 1000), random.randint(5, 7))
    dp = random.randint(0, 4)
    right_answer = round(n, dp)
    right_answer = str(right_answer)
    right_answers = [right_answer]
    input_message = str(n) + " rounded by " + str(10 ** (-dp)) + "(" + str(dp) + " d.p.) = "
    # ans=input(input_message)


def multiply_decimals():
    global ans, right_answers, input_message

    n = random.randint(0, 100)
    if random.randint(0, 1) == 1:
        n_sign = -1
    else:
        n_sign = 1

    m = round(random.randint(0, 12) * 10 ** random.randint(-3, 0), 4)
    right_answer = round(n_sign * n * m, 4)
    right_answers = [str(right_answer)]
    input_message = str(n * n_sign) + " * " + str(m) + " = "
    # ans=input(input_message)


def multiplication_table():
    global ans, right_answers, input_message
    # n*m
    n = random.randint(1, 11)
    m = random.randint(1, 11)
    right_answer = n * m
    right_answers = [str(right_answer)]
    input_message = str(n) + " * " + str(m) + " = "


def multiply_two_digits():
    global ans, right_answers, input_message
    # n*m
    n = random.randint(10, 100)
    m = random.randint(2, 11)
    right_answer = n * m
    right_answers = [str(right_answer)]
    input_message = str(n) + " * " + str(m) + " = "


def multiply_hundreds():
    # 26.05.2018 edition

    global ans, right_answers, input_message

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


# ans=input(input_message)


def find_sum():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def powers():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def factorization():
    global ans, input_message, right_answers

    def factorize(n):
        factorization.results = []
        i = 0
        divisor = 2

        while n > 1:
            if n % divisor == 0:
                factorization.results.append(divisor)
                n = n / divisor
                divisor = 2
            else:
                divisor += 1

                # generating proper muliples to form a number for further factorization

    prime_numbers_up_to_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97]

    n_1 = random.choice(prime_numbers_up_to_100[0:3])
    if random.randint(0, 1) == 1:
        n_2 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_2 = 1
    if random.randint(0, 1) == 1:
        n_3 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_3 = 1
    if random.randint(0, 1) == 1:
        n_4 = random.choice(prime_numbers_up_to_100[0:3])
    else:
        n_4 = 1
    if random.randint(0, 1) == 1:
        n_5 = random.choice(prime_numbers_up_to_100[0:4])
    else:
        n_5 = 1
    if random.randint(0, 1) == 1:
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
    # ans=input(input_message)


def linear_equations():
    global ans, right_answers, input_message
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
    # ans=input(input_message)


def linear_equations_lvl_2():
    global ans, right_answers, input_message
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
    # ans=input(input_message)


def division_remainders():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def fraction_reduction():
    import supportive_module
    global ans, right_answers, input_message

    common_factor = random.randint(1, 11)
    n_1 = random.randint(1, 13)
    n_2 = random.randint(1, 13)
    if n_1 % n_2 == 0:
        right_answer = str(int(n_1 / n_2))
    else:
        numerator = n_1 * common_factor
        denominator = n_2 * common_factor

        fraction_simplifier = supportive_module.fraction_simplifier
        fraction_simplifier(numerator, denominator)
        right_answer = str(fraction_simplifier.output)

    input_message = str(n_1 * common_factor) + "/" + str(n_2 * common_factor) + "= "
    right_answers = [right_answer]
    # ans=input(input_message)


def fractions_to_decimals():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def add_decimals_easy():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def percent_of():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def percent_of_no_calculation():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def percent_change():
    global ans, right_answers, input_message

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


def roots():
    global ans, right_answers, input_message

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


def logs():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def adding_fractions_easy():
    import supportive_module
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def division_mixed_fractions_easy():
    import supportive_module
    global ans, right_answers, input_message

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

    fraction_simplifier = supportive_module.fraction_simplifier
    crossout = supportive_module.crossout
    fraction_simplifier(divident, divisor)

    # converting fraction to a mixed number
    if crossout.top < crossout.bottom or crossout.bottom == 1:
        right_answer = fraction_simplifier.output
    else:
        whole = crossout.top // crossout.bottom
        fraction_top = crossout.top % crossout.bottom
        right_answer = str(whole) + " " + str(fraction_top) + "/" + str(crossout.bottom)
    # end converting fraction to a mixed number

    input_message = str(divident) + "/" + str(divisor) + " = "
    right_answers = [right_answer]
    # ans=input(input_message)


def division_mixed_fractions():
    import supportive_module
    global ans, right_answers, input_message

    # composing apropriate numbers
    divident = random.choice(
        [random.randint(80, 160),
         random.randint(80, 480),
         random.randint(80, 800)]
    )
    divisor = divident // random.randint(1, 10)

    fraction_simplifier = supportive_module.fraction_simplifier
    crossout = supportive_module.crossout
    fraction_simplifier(divident, divisor)

    # converting fraction to a mixed number
    if crossout.top < crossout.bottom or crossout.bottom == 1:
        right_answer = fraction_simplifier.output
    else:
        whole = crossout.top // crossout.bottom
        fraction_top = crossout.top % crossout.bottom
        right_answer = str(whole) + " " + str(fraction_top) + "/" + str(crossout.bottom)
    # end converting fraction to a mixed number

    input_message = str(divident) + "/" + str(divisor) + " = "
    right_answers = [right_answer]
    # ans=input(input_message)


def compare_two_numbers_easy():
    global ans, right_answers, input_message

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
    # ans=input(input_message)
    print(str(n2))


def multilply_two_digits():
    global ans, right_answers, input_message

    if random.randint(0, 1) == 1:
        n1 = random.randint(3, 13)
        n2 = random.randint(3, 13)
    else:
        n1 = int(round(random.triangular(1, 99, 25), 0))
        n2 = random.randint(0, 10)

    right_answer = str(n1 * n2)
    right_answers = [right_answer]
    input_message = str(n1) + " * " + str(n2) + " = "
    # ans=input(input_message)


def factorizing_square_of_sum():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def complete_square_easy():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def complete_square_a1():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def complete_square_a2():
    global ans, right_answers, input_message, prompt

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
    # ans=input(input_message)


def complete_square_a2_easy():
    global ans, right_answers, input_message, prompt

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
    # ans=input(input_message)


def complete_square_a3():
    global ans, right_answers, input_message, prompt

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
    # ans=input(input_message)


def complete_square_a4():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def complete_square_a5():
    global ans, right_answers, input_message, prompt

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
    # ans=input(input_message)


def star_count_easy():
    global ans, right_answers, input_message

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
    # ans=input(input_message)


def estimate():
    global ans, right_answers, input_message, prompt

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

    for i in range(1, max_species + 1):
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

        item_n(bottom, ceiling, max_repeat, i)
    input_message = g.question + '\n' * 2
    right_answer = str(g.estimate)
    right_answers = [right_answer]
    prompt = 'Estimate the sum,1 s.f. each:'
    print(prompt)
    print()
    # ans=input(input_message)


def complex_roots():
    global ans, right_answers, input_message, prompt
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
    # ans=input(input_message)
    # prompt='type r2(x) of square root of x'


def quadratic_equations_easy():
    global ans, right_answers, input_message, prompt

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

    # ans=input(input_message)


def quadratic_equations_calculator():
    global ans, right_answers, input_message, prompt

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

    # ans=input(input_message)


def value_function_quadratic():
    global ans, right_answers, input_message, prompt
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

    # ans=input(input_message)


def factoring_quadratics():
    global ans, right_answers, input_message, prompt

    import supportive_module
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



def convert_units():
    import supportive_module
    global ans, right_answers, input_message, prompt
    DELTA_RANGE = 10 #a power of 10 the range between the units to convert

    prefixes_dict = {'p': -12, 'n': -9, 'mc': -6, 'm': -3,
                     'c': -2, 'd': -1, 'u': 0,
                     'k': 3, 'M': 6, 'G': 9, 'T': 12}

    prefixes = list(prefixes_dict.keys())
    prefixes.remove('u')

    units = ['g', 'm', 's', 'N', 'J', 'W', 'A', 'Hz']

    unit = random.choice(units)

    n = random.randint(1, 100)
    k = random.choice([0.000001, 0.000005,
                       0.00001, 0.00005,
                       0.0005, 0.005, 0.01, 0.5,
                       0.0001, 0.001, 0.01, 0.1,
                       1, 5, 10, 50, 100, 500,
                       1000, 5000, 10000, 50000])

    value = n * k
    e_remover = supportive_module.e_remover
    value = e_remover(value)

    fixer = supportive_module.re_based_decimal_fixer
    if value % 1 == 0:
        value = str(int(value))
    else:
        value = fixer(str(value))

    okay = False
    while not okay:
        prefix_1 = random.choice(prefixes)
        prefix_2 = random.choice(prefixes)
        if prefix_2 != prefix_1:
            delta = prefixes_dict[prefix_1] - prefixes_dict[prefix_2]
            if abs(delta) < DELTA_RANGE:
                okay = True

    right_answer = float(value) * 10**delta
    if not right_answer % 1:
        right_answer = int(right_answer)


    if 'e' in str(right_answer):
        right_answer = "{:.16f}".format(right_answer)
        fixed = False
        while not fixed:
            if right_answer[-1] == '0':
                right_answer = right_answer[:-1]

    right_answer = str(right_answer)
    right_answers = [right_answer]


    if prefix_1 == 'u':
        prefix_1 = ''
    if prefix_2 == 'u':
        prefix_2 = ''

    prompt = 'Convert the following values to the new units:'
    input_message =  str(value) + ' ' + prefix_1 + unit + ' = ... ' + prefix_2 + unit + '\n'







# lists***lists***lists***lists***lists***lists***lists***lists***
exercises_list = [
    "Test",
    "Add negatives",
    "Round whole numbers",
    "Round decimals",
    "Multiply decimals",
    "Multiply hundreds",
    "Find sum",
    "Powers",
    "Factorization",
    "Linear equations",
    "Linear equations: level 2",
    "Division: remainders",
    "Fraction reduction",
    "Fractions to decimals",
    "Add decimals (easy)",
    "Percent of",
    "Percent of (no calculation)",
    "Percent change",
    "Roots",
    "Logs",
    "Adding fractions (easy)",
    "Division: mixed fractions (easy)",
    "Division: mixed fractions",
    "Compare two numbers (easy)",
    "Multiply two digits",
    "Factorizing square of sum",
    "Complete square (easy)",
    "Complete square A1",
    "Complete square A2 (easy)",
    "Complete square A2",
    "Complete square A3",
    "Complete square A4",
    "Complete square A5",
    "Star count (easy)",
    "Estimate sum",
    "Complex roots",
    "Quadratic equations (easy)",
    "Quadratic equations (calculator)",
    "Value of function: Quadratic",
    "Factoring Quadratics",
    "Multiply Two Digits",
    "Multiplication Table",
    "Convert Units"
]

exercises_dictionary = {
    "Test": test,
    "Add negatives": add_negatives,
    "Round whole numbers": round_whole_numbers,
    "Round decimals": round_decimals,
    "Multiply decimals": multiply_decimals,
    "Multiply hundreds": multiply_hundreds,
    "Find sum": find_sum,
    "Powers": powers,
    "Factorization": factorization,
    "Linear equations": linear_equations,
    "Linear equations: level 2": linear_equations_lvl_2,
    "Division: remainders": division_remainders,
    "Fraction reduction": fraction_reduction,
    "Fractions to decimals": fractions_to_decimals,
    "Add decimals (easy)": add_decimals_easy,
    "Percent of": percent_of,
    "Percent of (no calculation)": percent_of_no_calculation,
    "Percent change": percent_change,
    "Roots": roots,
    "Logs": logs,
    "Adding fractions (easy)": adding_fractions_easy,
    "Division: mixed fractions (easy)": division_mixed_fractions_easy,
    "Division: mixed fractions": division_mixed_fractions,
    "Compare two numbers (easy)": compare_two_numbers_easy,
    "Multiply two digits": multilply_two_digits,
    "Factorizing square of sum": factorizing_square_of_sum,
    "Complete square (easy)": complete_square_easy,
    "Complete square A1": complete_square_a1,
    "Complete square A2 (easy)": complete_square_a2_easy,
    "Complete square A2": complete_square_a2,
    "Complete square A3": complete_square_a3,
    "Complete square A4": complete_square_a4,
    "Complete square A5": complete_square_a5,
    "Star count (easy)": star_count_easy,
    "Estimate sum": estimate,
    "Complex roots": complex_roots,
    "Quadratic equations (easy)": quadratic_equations_easy,
    "Quadratic equations (calculator)": quadratic_equations_calculator,
    "Value of function: Quadratic": value_function_quadratic,
    "Factoring Quadratics": factoring_quadratics,
    "Multiply Two Digits": multiply_two_digits,
    "Multiplication Table": multiplication_table,
    "Convert Units": convert_units
}
