import sys

sys.stdin = open("in_out/chapter4/in1.txt", "rt")

def dfs(L, sum):
    global res
    if L == k:
        if sum==n:
            res += 1
    else:
        for i in range(coin_value[L]+1):
            dfs(L+1, sum+(coins[L] * i))

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    coins = []
    coin_value = []
    for i in range(k):
        d, p = map(int, input().split())
        coins.append(d)
        coin_value.append(p)

    res = 0
    dfs(0, 0)
    print(res)
