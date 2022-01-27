import sys

sys.stdin = open("in_out/section2/chapter8/in4.txt", "rt")


def reverse(x):
    temp_string = "".join(reversed(str(x)))
    return int(temp_string)


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True


def sol(n_list):
    result = list()
    for i in n_list:
        reversed_value = reverse(i)
        if isPrime(reversed_value):
            result.append(reversed_value)

    return result


n = int(input())
n_list = map(str, input().split())
result_list = sol(n_list)
for i in result_list:
    print(i, end=" ")
