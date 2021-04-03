class Solution:
    def solution(self, args: int) -> int:
        minus1, minus2 = 1, 0
        num = 0
        sum = 0
        while num < args:
            num = minus1 + minus2
            minus2 = minus1
            minus1 = num
            if num % 2 == 0:
                sum += num
        return sum


input = 4000000
print(Solution().solution(input))
