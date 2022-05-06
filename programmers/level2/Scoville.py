
def solution(scov, k):
    answer = 0
    while True:
        scov.sort()
        if scov[0] < k or scov[1] < k:
            first = scov.pop(0)
            second = scov.pop(0) * 2
            add = first + second
            scov.insert(0, add)
            answer += 1
    return answer

sco = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(sco, k))