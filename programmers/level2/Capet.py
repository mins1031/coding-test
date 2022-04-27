from collections import deque
def solution(brown, yellow):
    answer = []
    total_capet = brown + yellow
    divisors = deque([])
    for i in range(2, (total_capet // 2) + 1):
        if total_capet % i == 0:
            divisors.append(i)
    if divisors[0] == 2:
        divisors.popleft()
        divisors.pop()

    while divisors:
        # if len(divisors) == 1:
        left = divisors[0] - 2
        right = divisors[-1] - 2
        if (left * right) == yellow:
            answer.append(divisors[-1])
            answer.append(divisors[0])
            break
        else:
            divisors.popleft()
            divisors.pop()
        ''
    return answer

brown = 24
yellow = 24
brown2 = 8
yellow2 = 1
brown3 = 10
yellow3 = 2

print(solution(brown, yellow))
print(solution(brown2, yellow2))
print(solution(brown3, yellow3))
