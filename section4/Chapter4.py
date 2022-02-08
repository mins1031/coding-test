import sys

sys.stdin = open("in_out/chapter4/in2.txt", "rt")

n, c = map(int, input().split())
magootgan = list()
for i in range(n):
    magootgan.append(int(input()))

lt = min(magootgan)
rt = max(magootgan)
largest = max(magootgan)
result = 0
while lt <= rt:
    mid = (rt + lt) // 2
    temp = c * mid
    if temp > largest:
        rt = mid - 1
    else:
        lt = mid + 1
        result = mid

print(result)