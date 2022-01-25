import sys
sys.stdin = open("in_out/section2/chapter2/in3.txt", "rt")

def sol(n, s, e, k):
    a = n[s-1:e]
    a.sort()
    return a[k-1]


case = int(input())
for i in range(case):
    n_count, s, e, k = map(int, input().split())
    n = list(map(int, input().split()))
    print("#%d %d" %(i, sol(n, s, e, k)))
    print(i)
