import sys

sys.stdin = open("in_out/section2/chapter5/in5.txt", "rt")


def sol(n, m):
    temp_list = [0 for _ in range(41)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            tmp = i + j
            temp_list[tmp] = temp_list[tmp] + 1

    result = list()
    for i, v in enumerate(temp_list):
        if v == max(temp_list):
            result.append(i)
    result.sort()
    return result


n, m = map(int, input().split())
result = sol(n, m)
for i in result:
    print(i, end=" ")
