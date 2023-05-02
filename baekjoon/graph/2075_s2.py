import heapq
n = int(input())
n_list = list(map(int, input().split()))
heapq.heapify(n_list)

for i in range(n - 1):
    temp_n = list(map(int, input().split()))
    for j in temp_n:
        if n_list[0] < j :
            heapq.heappop(n_list)
            heapq.heappush(n_list, j)

print(n_list[0])