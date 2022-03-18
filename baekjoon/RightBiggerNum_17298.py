import sys
from collections import deque

n = sys.stdin.readline().rstrip()
right = deque(list(map(int, sys.stdin.readline().split(" "))))
rightBigger = [-1] * len(right)
stack = []
stack.append(right[0])
cursor = 0
res = []
for i in range(1, len(right)):
    if right[i] > stack[-1]:
        rightBigger[i-1] = right[i]
    elif stack[-1] >= right[i]:
        stack.append(right[i])

for i in rightBigger:
    print(i, end=' ')

