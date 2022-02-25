import sys


sys.stdin = open("in_out/chapter11/in5.txt", "rt")

def dfs(L, s):
    global res, cnt
    if L == k:
        if (sum(res) % m) == 0:
            cnt += 1
        return
    else:
        for i in range(s, n):
            res[L] = nums[i]
            dfs(L+1, i+1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())

    res = [0] * (k+1)
    cnt = 0
    dfs(0,0)
    print(cnt)
