import sys

sys.stdin = open("in_out/chapter15/in1.txt", "rt")

def dfs(L):
    global res
    if L == n:
        res += 1
        print(path)
    else:
        for i in range(1, n+1):
            if graph[L][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                ch[i] = 0
                path.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    res = 0
    for i in range(m):
        temp_node, temp_line = map(int, input().split())
        graph[temp_node][temp_line] = 1

    path = []
    path.append(1)
    ch[1] = 1
    dfs(1)
    print(res)