from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    while q:
        if len(q) == 1:
            answer += 1
            break
        hap = q[0] + q[-1]
        if hap > limit:
            q.pop()
            answer += 1
        else:
            q.pop()
            q.popleft()
            answer += 1

    return answer

p = [70, 50, 80, 50]
p2 = [70, 50, 80]
l = 100

print(solution(p2, l))

