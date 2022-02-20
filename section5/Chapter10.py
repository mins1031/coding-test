import sys
import heapq as hq

# sys.stdin.readline()
# sys.stdin = open("in_out/chapter10/in3.txt", "rt")

a = []
result = []
while True:
    n = sys.stdin.readline()
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            result.append(-1)
        else:
            result.append(hq.heappop(a))
    else:
        hq.heappush(a, n)

for i in result:
    print(i)
