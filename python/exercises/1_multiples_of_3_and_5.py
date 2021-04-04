# We're trying to find the sum of numbers divisible by 3 or 5
# starting at 3 and going up to `max_num`
def solution(max_num: int) -> int:
    # Loop from 3 (smallest possible answer) to `max_num`
    # and return the `answer`
    answer: int = 0
    for x in range(3, max_num):
        answer += x if (x % 3 == 0 or x % 5 == 0) else 0
    return answer
