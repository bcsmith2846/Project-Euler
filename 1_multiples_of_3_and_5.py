def solution(max_num: int) -> int:
    answer: int = 0
    for x in range(max_num):
        answer += x if (x % 3 == 0 or x % 5 == 0) else 0
    return answer


print(solution(1000))
