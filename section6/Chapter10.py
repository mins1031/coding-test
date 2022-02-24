import sys


sys.stdin = open("in_out/chapter10/in1.txt", "rt")

def dfs(L):
    global count
    if L == m:
        for i in res:
            print(i, end=' ')
        print()
        count += 1
    else:
        for i in marbles:
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    marbles = list()
    for i in range(1, n+1):
        marbles.append(i)
    res = [0] * m
    ch = [0] * (n+1)
    count = 0
    dfs(0)
    print(count)