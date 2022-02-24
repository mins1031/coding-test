import sys


sys.stdin = open("in_out/chapter7/in4.txt", "rt")
def dfs(L, sum):
    global change, smaller
    if L >= smaller:
        return
    if sum == change:
        if L < smaller:
            smaller = L
        return
    elif sum > change:
        return
    else:
        for i in coins:
            dfs(L + 1, sum + i)


if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)
    change = int(input())
    smaller = (change // max(coins)) + 1000
    dfs(0,0)
    print(smaller)
