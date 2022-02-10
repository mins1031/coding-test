import sys

sys.stdin = open("in_out/chapter4/in5.txt", "rt")

n, c = map(int, input().split())
magootgan = list()
for i in range(n):
    magootgan.append(int(input()))

magootgan.sort()

lt = 1
rt = magootgan[-1]
result = 0
while lt <= rt:
    mid = (rt + lt) // 2
    able_line_cnt = 1
    end = magootgan[0]
    for i in range(1, n):
        if (magootgan[i] - end) >= mid:
            able_line_cnt += 1
            end = magootgan[i]

    if able_line_cnt < c:
        rt = mid - 1
    else:
        lt = mid + 1
        result = mid

print(result)