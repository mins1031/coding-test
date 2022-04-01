from collections import deque

def solution(numbers):
    leng = len(numbers)
    answer = []

    def is_prime_find(n):
        n = int(n)
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


    for i in range(1, leng+1):
        for j in range(leng):
            if not is_prime_find("".join(numbers[0:i])):
                numbers = numbers[1:] + numbers[0]
            else:
                answer.append(int(numbers[0:i]))
                numbers = numbers[1:] + numbers[0]

    return len(set(answer))

numbers = "17"
# print(numbers[0:2])
# print("".join(numbers[0:2]))
# tt = numbers[1:] + numbers[0]
# print(tt)
print(solution(numbers))