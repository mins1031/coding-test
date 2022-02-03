# 리스트도 힙 처럼 pop, insert가 된다
# 또한 이차원리스트의 행에 새로운 리스트를 끼워넣을수 있다
import sys

sys.stdin = open("in_out/chapter8/in5.txt", "rt")


n = int(input())
gotgams = [list(map(int, input().split())) for _ in range(n)]

change_count = int(input())
for i in range(change_count):
    row, direct, distance = map(int, input().split())
    if direct == 0:
        for j in range(distance):
            gotgams[row-1].append(gotgams[row-1].pop(0))
    else:
        for j in range(distance):
            gotgams[row-1].insert(0, gotgams[row-1].pop())

standard = n // 2
lt = 0
rt = n
result = 0
for i in range(n):
    if i < standard:
        result += sum(gotgams[i][lt:rt])
        lt += 1
        rt -= 1

    else:
        result += sum(gotgams[i][lt:rt])
        lt -= 1
        rt += 1

print(result)
