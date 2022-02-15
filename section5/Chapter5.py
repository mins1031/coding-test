from collections import deque
import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")

n, m = map(int, input().split())

princies = deque([x+1 for x in range(n)])
cnt = 1
while len(princies) > 1:
    if cnt == m:
        princies.popleft()
        cnt = 1
    else:
        princies.append(princies.popleft())
        cnt += 1

print(princies[0])
