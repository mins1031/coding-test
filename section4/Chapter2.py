import sys

sys.stdin = open("in_out/chapter2/in1.txt", "rt")

n, k = map(int, input().split())
lines = list()
for i in range(n):
    lines.append(int(input()))

lt = 0
rt = max(lines)

while True:
    mid = (lt + rt) // 2
    standard = lines[mid]


