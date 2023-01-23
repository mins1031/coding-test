import sys

sys.stdin = open("in_out/chapter1/in5.txt", "rt")

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
lt = 0
rt = n
same_candy_max_count = 0

for i in range(n):
    mid = (lt + rt) // 2
    if n_list[mid] < m:
        lt = mid + 1
    elif n_list[mid] > m:
        rt = mid - 1
    else:
        same_candy_max_count = mid + 1

print(same_candy_max_count)
