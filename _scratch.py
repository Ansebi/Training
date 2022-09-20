import numpy as np
"""n(a + b) = na + nb"""
right_answers, input_message, prompt = None, None, None

alphabet = 'abcdefghijklmnopqrstuvwxyz'

    a, b = np.random.choice(list(alphabet), 2, replace=False)
    if a == b:
        print(a, b)

print('done')
