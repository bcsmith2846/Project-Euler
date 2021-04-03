import itertools


class Solution:
    def solution(self, num_digits: int) -> int:
        low = int('1' + '0' * (num_digits - 1))
        high = int('1' + '0' * num_digits)
        numbers = range(low, high)
        tuples = itertools.combinations_with_replacement(numbers, r=2)
        products = list(map(lambda m: m[0] * m[1], tuples))
        max = -1
        for product in reversed(products):
            if str(product) == str(product)[::-1]:
                if product > max:
                    max = product

        return max


input = 3
print(Solution().solution(input))
