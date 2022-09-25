import numpy as np
from support_module import num_to_str
from support_module import generate_target_sum
from support_module import list_to_str
import random

difficulty = 0
d = abs(difficulty)
"""
nax + nbx + ncx + nd + ne + nf = ngx + nhx + njx + nk + nm + np

solved as
n(a+b+c-g-h-j)x = n(k+m+p-d-e-f)
(a+b+c-g-h-j)x = k+m+p-d-e-f
or
effective_coef * x = effective_const

x = effective_const/effective_coef

x is pre-defined integer
"""
right_answers, input_message, prompt = None, None, None

for i in range(50):
    n_coefs = random.randint(1, 3 + d)
    n_consts = random.randint(1, 3 + d)
    n_coefs_left = random.randint(0, n_coefs)
    n_coefs_right = n_coefs - n_coefs_left
    # n_consts_left = random.randint(0, n_consts)
    # n_consts_right = n_consts - n_consts_left
    left_coefs = list(np.random.randint(1, 6 + d, n_coefs_left) * np.random.choice([-1, 1], n_coefs_left))
    right_coefs = list(np.random.randint(1, 6 + d, n_coefs_right) * np.random.choice([-1, 1], n_coefs_right))
    x = random.randint(-(7+d), 7+d)
    effective_coef = sum(left_coefs) - sum(right_coefs)
    effective_const = x * effective_coef
    sum_left_cts, sum_right_cts = generate_target_sum(effective_const, 2, 6 + d**2)
    sum_left_cts *= -1
    left_cts = generate_target_sum(sum_left_cts, random.randint(1, 2 + d), 5 + d**2)
    right_cts = generate_target_sum(sum_right_cts, random.randint(1, 2 + d), 5 + d**2)
    left_xs = [f'{i}x' for i in left_coefs]
    right_xs = [f'{i}x' for i in right_coefs]
    left = [i for i in list(left_xs + left_cts) if i]
    right = [i for i in list(right_xs + right_cts) if i]
    random.shuffle(left)
    random.shuffle(right)
    if not left:
        left = [0]
    if not right:
        right = [0]

    print()
    print(f'{x=}')
    left = list_to_str(left)
    right = list_to_str(right)
    print(f'{left} = {right}')




