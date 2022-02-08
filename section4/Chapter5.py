import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")

n = int(input())
meetings = list()
for i in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x : (x[1], x[0]))
temp = 0
count = 0

for ft,et in meetings:
    if temp <= ft :
        count += 1
        temp = et

print(count)
