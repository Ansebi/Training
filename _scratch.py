import numpy as np
from supportive_module import num_to_str
import random

difficulty = 0
d = abs(difficulty)
"""
forward: n(ax + by) = nax + nby
backward: nax + nby = n(ax + by)
"""
right_answers, input_message, prompt = None, None, None

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
mode = random.choice(['forward', 'backward'])
x, y = np.random.choice(list(alphabet), 2, replace=False)
a, b, n = np.random.randint(1, 6 + d) * np.random.choice([-1, 1], 3)
na = num_to_str(n*a, in_middle=False, remove_one=True)
nb = num_to_str(n*b, remove_one=True)
a = num_to_str(a, in_middle=False, remove_one=True)
b = num_to_str(b, remove_one=True)
state0 = f"n({a}{x} {b}{y})"
state1 = f"{na}{x} {nb}{y}"
prompt = 'Open the brackets. Example: 5(x + 2y) = 5x + 10y'
if mode == 'backward':
    state0, state1 = state1, state0
    prompt = 'Factorize the following. Example: 5x + 10y = 5(x + 2y)'
input_message = f"{state0} = "
right_answers = [state1]


