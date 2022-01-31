import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")


def sol(n, m, n_list):
    # for i in range(n):
    #     tmp_sum = n_list[i]
    #     for j in range(i+1, n):
    #         tmp_sum += n_list[j]
    #         if tmp_sum == m:
    #             res += 1
    #             break
    #         elif tmp_sum > m:
    #             break
    # 이중포문 이제 부터 지양하면서 구현해보자
    res = 0
    lt = 0
    rt = 1
    total = 0

    while True:
        total = n_list[lt]
        if total < m:
            total += n_list[rt]
        if total == m :
            res += 1
            lt += 1
            rt = lt + 1

        total += n_list[lt]
    return res


n, m = map(int, input().split())
n_list = list(map(int, input().split()))

print(sol(n, m, n_list))
