import importlib
import unittest
import random
from scaffold import *
module = importlib.import_module('exercises.1_multiples_of_3_and_5')


class TestExerciseOne(unittest.TestCase):
    def test_three_and_five(self):
        # Base cases and exercise question
        data = [0, 1, 3, 5, 10, 20, 100, 1000]
        # Create 250 random integers in the range of `0..5000`
        data.extend([i for i in random_int_iterator(0, 5000, 250)])
        # For each element in data find the sum of the numbers
        # `3..(data[j] - 1)` where the number is divisible by 3 or 5
        answers = [sum([i for i in range(3, data[j])
                        if i % 5 == 0 or i % 3 == 0])
                   for j in range(len(data))]
        # Loop over our generated answers and make sure our
        # solution function returns the name number.
        for i, datum in enumerate(data):
            self.assertEqual(module.solution(datum), answers[i])

    # Create a generator iterable to return `amount` random numbers
    # in the range `low..high`
