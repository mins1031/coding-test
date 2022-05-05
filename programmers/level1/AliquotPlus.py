def get_aliquot(num):
    count = 2
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i == 1:
            answer -= 1
            continue
        if get_aliquot(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

left = 13
right = 17

print(solution(1, 2))