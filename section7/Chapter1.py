import sys

sys.stdin = open("in_out/chapter1/in2.txt", "rt")


def dfs(L, total, sum_time, c):
    global res
    if limit_time <= sum_time:
        if total > res:
            res = total
        return
    else:
        for i in range(c, n+1):
            dfs(L + 1, total + score[i-1], sum_time + time[i-1], c+i)


if __name__ == "__main__":
    n, limit_time = map(int, input().split())
    score = list()
    time = list()
    res = 0

    for i in range(n):
        tmp_s, tmp_t = map(int, input().split())
        score.append(tmp_s)
        time.append(tmp_t)

    dfs(0, 0, 0, 1)
    print(res)
