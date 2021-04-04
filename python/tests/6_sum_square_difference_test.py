import importlib
from python.tests.scaffold import random_int_iterator
import unittest
import random
from scaffold import *
module = importlib.import_module('exercises.6_sum_square_difference')


class TestExerciseOne(unittest.TestCase):
    def test_difference(self):
        # Create a list of 100 random integers
        # in the range `0..250`
        test_data = [i for i in random_int_iterator(0, 250, 100)]
        # Generate answers to the random numbers above
        test_answers = [((sum([i for i in range(1, test_data[j] + 1)]) ** 2) -
                         (sum(i ** 2 for i in range(1, test_data[j] + 1))))
                        for j in range(len(test_data))]
        # Check that our solution give the same answers.
        for i, datum in enumerate(test_data):
            self.assertEqual(
                test_answers[i], module.Solution().solution(datum))
