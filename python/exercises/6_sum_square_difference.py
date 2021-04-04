from typing import List, Tuple
import math
import itertools
from functools import reduce

# Find the difference betwenn the square of the sums of the numbers
# `1..end` and the sum of the squares of the numbers `1..end`
#
# Sum of the squares 1..10:
#       1^2 + 2^2 + ... + 10^2 = 385
# Square of the sums 1..10:
#       (1 + 2 + ... + 10)^2 = 3025


class Solution:

    def solution(self, end: int) -> int:
        sqOfSu = sum(range(1, end+1)) ** 2
        suOfSq = sum([i ** 2 for i in range(1, end + 1)])
        return sqOfSu - suOfSq


print(Solution().solution(100))
