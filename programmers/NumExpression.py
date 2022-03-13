def solution(n):
    answer = 0
    sum = 0
    num = 1
    fix = num
    while True:
        sum += num
        num += 1
        if fix > n:
            break
        if sum == n:
            answer += 1
            num = fix + 1
            sum = 0
            fix += 1
        elif sum > n:
            sum = 0
            num = fix + 1
            fix += 1

    return answer

print(solution(15))

