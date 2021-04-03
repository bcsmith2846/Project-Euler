import itertools


class Solution:
    # Template method for soultions
    def solution(self, num_digits: int) -> int:
        # Create low and high bounds from the number of digits given
        # Ex: `num_digits = 2`
        #       low     = '1' + ('0' * (2-1)) = '1' + '0' * 1 = '1' + '0' = '10'
        #       high    = '1' + ('0' * 2) = '1' + '00' = '100'
        low = int('1' + '0' * (num_digits - 1))
        high = int('1' + '0' * num_digits)
        # Return all the numbers with `num_digits` number of digits
        numbers = range(low, high)
        # Return all length `r=2` combinations of numbers with `num_digits` digits.
        # We don't want permutations or cartesian product; we don't want to repeat
        # tuples that are the same but reversed, but we do want tuples to be able
        # to contain the same number twice
        #
        # Ex:
        #       bad: (123, 321) AND (321, 123)
        #       good: (111, 111)
        #
        # This means we want combinations with replacement (allowing the same number to
        # be picked again)
        #
        tuples = itertools.combinations_with_replacement(numbers, r=2)
        # Map the tuples to their products
        products = list(map(lambda m: m[0] * m[1], tuples))
        # Loop over the products searching for palindromes larger than `max`
        max = -1
        for product in reversed(products):
            if str(product) == str(product)[::-1]:
                if product > max:
                    max = product

        return max


# Boilerplate runner code
input = 3
print(Solution().solution(input))
