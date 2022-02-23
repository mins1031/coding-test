import sys

sys.stdin = open("in_out/chapter5/in5.txt", "rt")


def dfs(L, sum, total_sum):
    global largest
    if sum >= c:
        return
    # 밑의 조건문은 원래 없었다. in5는 시간이 너무 많이 걸렸다. 그 해결책이 밑의 조건문.
    # 재귀를 하며 지금까지 온 내용의 합을 계속 구한다. 그렇게 해서 [전체합] - [현재까지 합] + [선택된 내용의 합] 을 하면 지금까지 합해진 내용의 최대값을 알수 있게된다.
    # 이 최대값이 제일 큰무게보다 작다면 계속 진행하나 마나이기 때문에 거기서 바로 리턴시켜 재귀 횟수를 줄일수 있게되고 시간이 단축되게 된다.
    if (total - total_sum + sum) < largest:
        return
    if L == n:
        if sum > largest:
            largest = sum
    else:
        dfs(L + 1, sum + weight[L], total_sum+weight[L])
        dfs(L + 1, sum, total_sum+weight[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = list()
    largest = -214700000000
    for _ in range(n):
        weight.append(int(input()))
    total = sum(weight)
    dfs(0, 0, 0)
    print(largest)
