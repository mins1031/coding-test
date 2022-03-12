import sys

sys.stdin = open("in_out/chapter1/in1.txt", "rt")

def recur(n):
    if line[n] > 0 :
        return line[n]
    if n == 1 or n == 2:
        return n
    line[n] = recur(n-1) + recur(n-2)
    return line[n]

n = int(input())
line = [0] * (n+1)
print(recur(n))