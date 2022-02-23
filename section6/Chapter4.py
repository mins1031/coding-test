import sys

sys.stdin = open("in_out/chapter4/in5.txt", "rt")


def dfs(L, sum):
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        dfs(L+1, sum+a[L])
        dfs(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    dfs(0, 0)
    print("NO")