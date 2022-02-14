import sys

sys.stdin = open("in_out/chapter1/in2.txt", "rt")


n, m = input().split()

n = list(map(int, n))
m = int(m)

stack = [n[0]]
lt = 0

for i in range(1, len(n)):
    while stack[-1] < n[i] and stack:
        stack.pop()
        m -= 1
    stack.append(n[i])
    if m == 0:
        stack.extend(n[i:])
        break

for i in stack:
    print(i, end='')



