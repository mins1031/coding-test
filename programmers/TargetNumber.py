def solution(numbers, target):
    answer = 0
    def dfs(L):
        nonlocal answer
        if L == len(numbers):
            if sum(numbers) == target:
                answer += 1
        else:
            numbers[L] = numbers[L] * -1
            dfs(L + 1)
            numbers[L] = numbers[L] * -1
            dfs(L+1)
    dfs(0)
    return answer

list1 = [1, 1, 1, 1, 1]
target1 = 3

list2 = [4, 1, 2, 1]
target2 = 4

print(solution(list2, target2))