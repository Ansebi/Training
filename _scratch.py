number = '0.01'
number = float(number)

class NotInRangeError(Exception):
    '''the value is not supported (too large or too small)'''

    def __init__(self, message= 'the value has to be between 10**-13 and 10**13'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

if not 10**-13 < number < 10**13:
    raise NotInRangeError

magnitude = None
for power in range(-13, 14):
    if 10**power > number:
        magnitude = power
        break

print(magnitude)
