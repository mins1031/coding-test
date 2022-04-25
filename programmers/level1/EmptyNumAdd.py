def solution(numbers):
    tmp = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    numbers = set(numbers)
    res = tmp - numbers
    return sum(res)

def solution2(numbers):
    numbers = set(numbers)
    return 45 - sum(numbers)


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers))
