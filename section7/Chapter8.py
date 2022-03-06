import sys
from collections import deque

sys.stdin = open("in_out/chapter8/in5.txt", "rt")

def bfs(n):
    stand = n // 2
    sum = apple_trees[stand][stand]
    deq = deque()
    deq.append((stand, stand))
    ch[stand][stand] = 1
    L = 0
    while True:
        if L == stand:
            break
        size = len(deq)
        for i in range(size):
            tmp = deq.popleft()
            for j in range(4):
                x = tmp[0] + point[j][0]
                y = tmp[1] + point[j][1]
                if ch[x][y] == 0:
                    ch[x][y] = 1
                    sum += apple_trees[x][y]
                    deq.append((x,y))

if __name__ == "__main__":
    point = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    n = int(input())
    apple_trees = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    print(bfs(n))

# 기존코드 요건 bfs가 아님 stand = n // 2
# s = e = stand
# res = 0
# for i in range(n):
#     for j in range(s, e + 1):
#         res += apple_trees[i][j]
#     if i >= stand:
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
# return res
