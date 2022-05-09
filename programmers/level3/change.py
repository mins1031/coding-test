def solution(n, money):
    answer = 0
    leng = len(money)

    def dfs(L, sum, leng):
        nonlocal answer, n
        if sum >= n:
            if sum > n:
                return
            else:
                answer += 1
                return
        else:
            for i in money:
                dfs(L + 1, sum + i, leng)

    dfs(0, 0, leng)
    return answer


n = 5
money = [1, 2, 5]
print(solution(n, money))
