import sys

sys.stdin = open("in_out/chapter2/in5.txt", "rt")

n, k = map(int, input().split())
lines = list()
for i in range(n):
    lines.append(int(input()))

lt = 0
rt = max(lines)
same_candy_max_count = 0
while lt <= rt:
    mid = (lt + rt) // 2

    temp_total = 0
    for i in lines:
        temp_total += i // mid

    if temp_total >= k:
        lt = mid + 1
        same_candy_max_count = mid
    else:
        rt = mid - 1

print(same_candy_max_count)
