import sys

sys.stdin = open("in_out/chapter1/in4.txt", "rt")


def dfs(L, total, sum_time):
    global res
    if sum_time > limit_time :
        return
    if L == n :
        if total > res:
            res = total
    else:
        dfs(L + 1, total + score[L], sum_time + time[L])
        dfs(L + 1, total, sum_time)


if __name__ == "__main__":
    n, limit_time = map(int, input().split())
    score = []
    time = []
    res = 0
    for i in range(1, n+1):
        tmp_s, tmp_t = map(int, input().split())
        score.append(tmp_s)
        time.append(tmp_t)

    dfs(0, 0, 0)
    print(res)
