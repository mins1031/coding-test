import sys

sys.stdin = open("in_out/chapter1/in5.txt", "rt")

def sol(x):
    if x <= 1:
        print(x, end="")
        return
    sol(x // 2)
    print(x % 2, end="")

n = int(input())
sol(n)
