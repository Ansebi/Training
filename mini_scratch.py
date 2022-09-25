from support_module import get_var_chars
from support_module import num_to_str


def list_to_str(raw_list) -> str:
    """
    :param raw_list: a list of floats, integers, numeric strings or strings like '-5x'
    :return: ['8', '-5x', 2] returns '8 -5x + 2'
    """
    processed_list = []
    for n, i in enumerate(raw_list):
        var_char = get_var_chars(str(i))
        contains_variable = True if var_char else False
        if contains_variable:
            i = i.replace(var_char, '')
        try:
            i = float(i)
        except:
            warning = f"Wrong data type of the element: {i}.\n"
            warning += "Must be a float or an integer, a numeric string at least.\n"
            warning += "Or something like '5x' or '-4a'. These are supported and are a reason to make this function."
            print(warning)
        in_middle = True if n else False
        i = num_to_str(i, in_middle=in_middle, remove_one=contains_variable) + var_char
        processed_list.append(i)
    return ' '.join(processed_list)


# print('5x'.replace(get_var_chars('-5'), ''))
example = [8.15, '-1x', -3, -2, -1, '3x', 5.0]
print(list_to_str(example))

