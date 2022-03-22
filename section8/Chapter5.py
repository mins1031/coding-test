import sys

sys.stdin = open("in_out/chapter5/in2.txt", "rt")

n = int(input())
array = list(map(int, input().split()))
standard = sorted(array)
dy = [0] * n
dy[0] = 1
for i in range(n):
    tmp_max = 0

    for j in range(i-1, -1, -1):
        if array[i] > array[j]:
            if dy[j] > tmp_max:
                tmp_max = dy[j]
    dy[i] = tmp_max + 1

print(max(dy))