import sys
import heapq as hq

# sys.stdin.readline()
sys.stdin = open("in_out/chapter11/in2.txt", "rt")

a = []
same_candy_max_count = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            same_candy_max_count.append(-1)
        else:
            same_candy_max_count.append(abs(hq.heappop(a)))
    else:
        hq.heappush(a, -n)

for i in same_candy_max_count:
    print(i)
