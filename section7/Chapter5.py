import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")


def dfs(L):
    global res
    if L == n:
        cha = max(people) - min(people)
        if cha < res:
            tmp=set()
            for x in people:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            people[i] += coins[L]
            dfs(L + 1)
            people[i] -= coins[L]


if __name__ == "__main__":
    n = int(input())
    coins = []
    people = [0] * 3
    for i in range(n):
        d = int(input())
        coins.append(d)

    res = 2147000000
    dfs(0)
    print(res)
