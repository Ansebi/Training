import numpy as np
from supportive_module import num_to_str
from supportive_module import generate_target_sum
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

n_coefs = random.randint(1, 3 + d)
n_consts = random.randint(1, 3 + d)
n_coefs_left = random.randint(0, n_coefs)
n_coefs_right = n_coefs - n_coefs_left
n_consts_left = random.randint(0, n_consts)
n_consts_right = n_consts - n_consts_left

print(f"{'a' * n_coefs_left}{'1' * n_consts_left} = {'a' * n_coefs_right}{'1' * n_consts_right}")
left_coefs = np.random.randint(1, 6 + d, n_coefs_left) * np.random.choice([-1, 1], n_coefs_left)
right_coefs = np.random.randint(1, 6 + d, n_coefs_right) * np.random.choice([-1, 1], n_coefs_right)
print([f'{i}x' for i in left_coefs], '=', [f'{i}x' for i in right_coefs])
x = random.randint(-(7+d), 7+d)
effective_coef = sum(left_coefs) - sum(right_coefs)
effective_const = x * effective_coef
sum_left_const, sum_right_const = generate_target_sum(sum_left_const, random.randint(1, 3 + d), 5 + d**2)
sum_left_const *= -1
left_constants = generate_target_sum(effective_const, 2, 6 + d**2)
print(f'{x=}')
print(sum(left_coefs), sum(right_coefs), effective_coef)
print(f'{sum_left_const=}, {sum_right_const=}')
print(generate_target_sum(x*effective_coef, 4, 80))




