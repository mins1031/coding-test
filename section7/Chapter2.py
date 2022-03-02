import sys

sys.stdin = open("in_out/chapter2/in5.txt", "rt")


def dfs(L, sum_pay):
    global res
    if L == n:
        if res < sum_pay:
            res = sum_pay
    elif L < n:
        return
    else:
        dfs(L + day[L], sum_pay + pay[L])
        dfs(L + 1, sum_pay)


if __name__ == "__main__":
    n = int(input())
    day = [0] * (n + 1)
    pay = [0] * (n + 1)
    for i in range(n):
        d, p = map(int, input().split())
        day[i] = d
        pay[i] = p

    res = 0
    dfs(0, 0)
    print(res)
