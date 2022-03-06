from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        visited[now] = 1
        for i in links[now]:
            if visited[i] == 0:
                q.append(i)


computer = int(input())
link_cnt = int(input())
links = [[] for _ in range(computer+1)]
visited = [0] * (computer+1)

for i in range(link_cnt):
    n, m = map(int, input().split())
    links[n].append(m)
    links[m].append(n)

bfs(1)
cnt = 0
for i in visited:
    if i == 1:
        cnt += 1
print(cnt-1)

