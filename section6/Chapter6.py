import sys

sys.stdin = open("in_out/chapter6/in1.txt", "rt")


def dfs(L):
    global result, count
    if m == L:
        count += 1
        for i in result:
            print(i, end=' ')
        print()
        return
    else:
        for i in range(1, n+1):
            result[L] = i
            dfs(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    intArray = list()
    result = [0] * m
    count = 0
    dfs(0)
    print(count)
