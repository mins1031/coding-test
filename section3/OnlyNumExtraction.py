import sys


sys.stdin = open("in_out/chapter2/in5.txt", "rt")

def sol(n):
    temp = ""
    for i in n:
        if i.isdigit():
            temp += i

    result = int(temp)
    print(result)

    count = 2
    for i in range(2,result):
        if result%i == 0:
            count += 1

    print(count)
n = input()
sol(n)
