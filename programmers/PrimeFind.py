from collections import deque

def solution(numbers):
    leng = len(numbers)

    def is_prime_find(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # def dfs(L, ):
    #     if L == leng:
    #         return
    #     else:
    #         for i in
    #


    answer = 0
    return answer

numbers = "011"
print(numbers[0])
print(numbers[1])
print(numbers[0:2])
solution(numbers)