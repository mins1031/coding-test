# 실패!
# def solution(n):
#     nums = [0] * (n+1)
#     def recur(n):
#         if nums[n] > 0:
#             return nums[n]
#         if n == 1 or n == 0:
#             return n
#         nums[n] = recur(n-1) + recur(n-2)
#         return nums[n]
#     answer = recur(n)
#     return answer

def solution(n):
    cache = [0 for i in range(n + 1)]
    cache[0] = 0
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) & 1234567

    answer = cache[n]
    return answer

n = 3
n2 = 5
print(solution(n2))
