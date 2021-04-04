import os
import sys
import random
if os.path.abspath('python') not in sys.path:
    sys.path.append(os.path.abspath('python'))


def random_int_iterator(low: int, high: int, amount: int):
    for x in range(amount):
        yield random.randint(low, high)
