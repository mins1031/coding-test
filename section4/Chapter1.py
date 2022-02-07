import sys

sys.stdin = open("in_out/chapter1/in5.txt", "rt")

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
lt = 0
rt = n
result = 0

for i in range(n):
    mid = (lt + rt) // 2
    if n_list[mid] < m:
        lt = mid + 1
    elif n_list[mid] > m:
        rt = mid - 1
    else:
        result = mid + 1

print(result)
