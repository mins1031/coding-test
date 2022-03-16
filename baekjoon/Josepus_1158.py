import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
circle = deque()
jose = []
for i in range(1, n+1):
    circle.append(i)

cnt = 0
while circle:
    if cnt == k-1:
        jose.append(circle.popleft())
        cnt = 0
    else:
        circle.append(circle.popleft())
        cnt += 1

print("<" + str(jose)[1:-1] + ">")



