import sys
import heapq as hq

# sys.stdin.readline()
sys.stdin = open("in_out/chapter11/in2.txt", "rt")

a = []
result = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            result.append(-1)
        else:
            result.append(abs(hq.heappop(a)))
    else:
        hq.heappush(a, -n)

for i in result:
    print(i)
