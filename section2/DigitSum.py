import sys


sys.stdin = open("in_out/section2/chapter6/in5.txt", "rt")

def sol(numbers):
    result = 0
    bigger = 0
    for i in numbers:
        tmp = calculateDigitSum(i)
        if tmp > bigger:
            bigger = tmp
            result = i

    return result


def calculateDigitSum(i):
    tmp = 0
    for j in i:
        tmp = tmp + int(j)
    return tmp


n = int(input())
numbers = map(str, input().split())

print(sol(numbers))
