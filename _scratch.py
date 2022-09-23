import numpy as np
# from supportive_module import num_to_str
# import random
#
# difficulty = 0
# d = abs(difficulty)
# """
# nax + nbx + ncx + nd + ne + npf = ngx + nhx + njx + nk + nm + np
# """
# right_answers, input_message, prompt = None, None, None
#
# n_coefs = random.randint(1, 3 + d)
# n_consts = random.randint(1, 3 + d)
# n_coefs_left = random.randint(0, n_coefs)
# n_coefs_right = n_coefs - n_coefs_left
# n_consts_left = random.randint(0, n_consts)
# n_consts_right = n_consts - n_consts_left
#
# print(f"{'a' * n_coefs_left}{'1' * n_consts_left} = {'a' * n_coefs_right}{'1' * n_consts_right}")
# left_coefs = np.random.randint(1, 6 + d, n_coefs_left) * np.random.choice([-1, 1], n_coefs_left)
# right_coefs = np.random.randint(1, 6 + d, n_coefs_right) * np.random.choice([-1, 1], n_coefs_right)
# print([f'{i}x' for i in left_coefs], '=', [f'{i}x' for i in right_coefs])
# x = random.randint(-(7+d), 7+d)
# print('x', x)
# print(sum(left_coefs), sum(right_coefs), sum(left_coefs)-sum(right_coefs))
#


def generate_target_sum(target: int, n: int, spread: int) -> list:
    """
    requires: numpy as np
    returns: a list of integers

    given the target 5 and n=2 it would propose e.g. [2, 3] which add up to 5
    range controls the deviation of the generated addends
    """
    addends = (np.random.randint(1, max(1, spread+1), n) * np.random.choice([1, -1], n) + target / n).astype(int)
    delta = target - addends.sum()
    for i in range(abs(delta)):
        addends[i % n] += delta//abs(delta)
    return list(addends)


print(generate_target_sum(6, 4, 8))




