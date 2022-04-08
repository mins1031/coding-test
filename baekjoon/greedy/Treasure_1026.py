import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
b = list(map(int, sys.stdin.readline().rstrip().split()))
b.sort(reverse=True)

res = 0

for i in range(n):
    res += a[i] * b[i]

print(res)