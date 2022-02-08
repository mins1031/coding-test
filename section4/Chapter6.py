import sys

sys.stdin = open("in_out/chapter6/in4.txt", "rt")

n = int(input())
players = list()
for i in range(n):
    s, e = map(int, input().split())
    players.append((s, e))

players.sort(reverse=True)

wig = 0
count = 0
for i in players:
    temp = i[1]
    if temp > wig:
        count += 1
        wig = temp

print(count)

