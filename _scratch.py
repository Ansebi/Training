import numpy as np

"""
ax + by = n1
cy + dz = n2
ez + fx = n3
"""
right_answers, input_message, prompt = None, None, None

a, b, c, d, e, f, x, y, z = np.random.randint(-11, 11, 9)

n1 = a * x + b * y
n2 = c * y + d * z
n3 = e * z + f * x


def num_to_str(n, in_middle=True):
    if n < 0:
        return str(n)
    else:
        if in_middle:
            return f'+ {n}'
        else:
            return str(n)


line1 = f'{a}x {num_to_str(b)}y = {n1}'
line2 = f'{c}y {num_to_str(d)}z = {n2}'
line3 = f'{e}z {num_to_str(f)}x = {n3}'

input_message = '\n'.join([line1, line2, line3])
prompt = 'Find x, y, z. Response Example: 5, -5, 10'
right_answers = [f'{x}, {y}, {z}']

