import sys

sys.stdin = open("in_out/chapter6/in5.txt", "rt")


def sol(n, a):
    sums = list()
    sum3 = 0
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(n):
            if i == j:
                sum3 = a[i][j]
            sum1 += a[i][j]
            sum2 += a[j][i]
        sums.append(sum1)
        sums.append(sum2)
    sums.append(sum3)

    tmp = n - 1
    sum4 = 0
    for i in range(n):
        sum4 += a[i][tmp]
        tmp -= 1

    sums.append(sum4)
    return max(sums)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

print(sol(n, a))
