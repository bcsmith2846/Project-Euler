import math

# We're trying to find the largest prime factor of a
# given input, `num`


class Solution:
    def solution(self, num: int) -> int:
        prime_factors = []
        n = num

        # Take care of the even prime factors (2), and remove
        # all even non-prime factors from the process.
        while n % 2 == 0:
            prime_factors.append(2)
            n //= 2
        # All remaining factors to produce primes must be
        # odd (not 2).
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                prime_factors.append(i)
                n //= i
        # If num is prime, it n won't go below 2, so add num.
        if n > 2:
            prime_factors.append(num)

        return max(prime_factors)
