import sys

sys.stdin = open("in_out/chapter9/in5.txt", "rt")

n, k = map(int, input().split())
jewel = []
for i in range(n):
    w, v = map(int, input().split())
    jewel.append((w, v))

dy = [0] * (k+1)
for w, v in jewel:
    for i in range(w, k+1):
        if dy[i] < dy[i-w] + v :
            dy[i] = dy[i-w] + v

print(max(dy))
dy = [0] * (k+1)
for i in range(n):
    w,v = map(int, input().split())
    for j in range(w, k+1):
        dy[j] = max(dy[j], dy[j-w] + v)
print(dy[k])






