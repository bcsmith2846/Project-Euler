import itertools
from typing import Tuple, List
import math

# We want to find the smallest number that is divisible by
# all of the numbers in `some_range`.


class Solution:
    def solution(self, input_range: Tuple[int, int]) -> int:
        # One divides everything and we disallow negative numbers
        if input_range[0] < 2:
            input_range = 2, input_range[1]
        # The list of possible divisors in the range of
        # `input_range[0]...input_range[1]` (inclusive)
        divisors = list(range(input_range[0], input_range[1] + 1))
        divisors.sort()
        # These loops weed out the numbers that are factors
        # of some larger number.
        #
        # We use all of the numbers in the range as dividends and
        # check if the number can be divided by any of the numbers
        # in the range that are smaller than it.
        #
        # Example:
        #       10 divides 20, so we don't need to check if 10
        #       divides the current number we are trying.
        for dividend in range(input_range[0], input_range[1] + 1):
            for divisor in range(input_range[0], dividend):
                if dividend % divisor == 0:
                    if divisor in divisors:
                        divisors.remove(divisor)
        # Count numbers starting with the largest divisor doubled
        # and step by the largest divisor. This optimization is based
        # On the fact that 1) if there is only one divisor, then the
        # smallest divisor is that number and 2) the answer must be
        # divisible by the largest divisor, so we only need consider
        # the multiples of it.
        answers: List[int] = []
        for number in itertools.count(divisors[-1] * 2, divisors[-1]):
            all = True
            for divisor in divisors:
                if number % divisor != 0:
                    all = False
                    continue
            if all:
                return number
        return -1


# Boilerplate driver code
input = (1, 20)
print(Solution().solution(input))
