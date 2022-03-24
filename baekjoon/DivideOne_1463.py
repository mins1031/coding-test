n = int(input())

dy = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    dy[i] = dy[i - 1] + 1
    if i % 2 == 0 and dy[i // 2] + 1 < dy[i]:
        dy[i] = dy[i // 2] + 1

    if i % 3 == 0 and dy[i // 3] + 1 < dy[i]:
        dy[i] = dy[i // 3] + 1

print(dy[n])
