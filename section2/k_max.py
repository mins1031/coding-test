import sys


sys.stdin = open("in_out/chapter3/in5.txt", "rt")

def sol(n, k, temp_list):
    if len(temp_list) != n:
        return -1

    total_sum = set()
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for p in range(j+1, n):
                total = temp_list[i] + temp_list[j] + temp_list[p]
                total_sum.add(total)

    total_sum = list(total_sum)
    total_sum.sort(reverse=True)
    return total_sum[k-1]


n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

print(sol(n, k, temp_list))
