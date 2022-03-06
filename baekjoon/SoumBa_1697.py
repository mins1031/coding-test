from collections import deque

# def dfs(L, present):
#     if present == k:
#         print(L)
#         return
#     else:
#         visited[present] = 1
#         for i in (present + 1, present - 1, present * 2):
#             if visited[i] == 0:
#                 dfs(L+1, i)

def bfs(present):
    q = deque([present])
    while q:
        now = q.popleft()
        if now == k:
            return visited[now]

        for i in (now+1, now-1, now*2):
            if not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)


n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n))
# dfs(0, n)