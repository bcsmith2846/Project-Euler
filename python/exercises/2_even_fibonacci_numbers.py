# We're trying to find the sum of the even fibonacci numbers
# from 1 to `max_num`
class Solution:
    # We're going to do fibonacci iteratively
    def solution(self, max_num: int) -> int:
        # `minus1` and `minus2` keep track of the last two values
        # starting with 0 and 1, `num` keeps track of the current
        # value, and `sum` is a running sum of `num`'s even values.
        #
        minus1, minus2 = 1, 0
        num = 0
        sum = 0
        while num < max_num:
            num = minus1 + minus2
            minus2 = minus1
            minus1 = num
            # We only care to sum even values of `num`
            if num % 2 == 0:
                sum += num
        return sum
