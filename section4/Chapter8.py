import sys
from collections import deque

sys.stdin = open("in_out/chapter8/in1.txt", "rt")


n, m = map(int, input().split())
pasengers = list(map(int, input().split()))

pasengers.sort()

lt = 0
rt = n - 1
temp_list = [False] * n
res = 0

pasengers = deque(pasengers)

while pasengers:
    if len(pasengers) == 1:
        res += 1
        break

    temp_sum = pasengers[0] + pasengers[-1]
    if temp_sum > m:
        pasengers.pop()
        res += 1
    else:
        pasengers.popleft()
        pasengers.pop()
        res += 1

print(res)