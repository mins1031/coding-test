'''
그래프 : 노드와 간선으로 이루어진 트리
무방향그래프 : 방향에 상관없이 간선이 연결된 노드는 서로 왔다갔다 할수 있는 그래프.
가중치 방향 그래프 : 각 노드별로 이동할수 있는 방향이 간선으로 표기되고 각 간선의 값도 표기되어있는 그래프

'''
''' 
무방향 그래프 구현
5 5
1 2
1 3
2 4
3 4
4 5

n, m = map(int, input().split())
g=[[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
'''
'''
가중치 방향 그래프 구현
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
'''
n, m = map(int, input().split())
g=[[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()