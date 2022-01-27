import sys


sys.stdin = open("in_out/section2/chapter7/in5.txt", "rt")

def sol(n, n_list):
    count = 0
    for i in range(2, n+1):
        if n_list[i] == 0:
            count += 1
            for j in range(i, n+1, i):
                n_list[j] = 1

    return count


n = int(input())
n_list = [0 for _ in range(n+1)]

print(sol(n, n_list))
