import heapq as hq
import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(a) == 0:
            print(0)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
