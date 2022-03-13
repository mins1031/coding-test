def solution(land):
    answer = 0
    ch = [0 for _ in range(col)]
    def dfs(L, sum):
        nonlocal answer
        if L == len(land):
            if sum > answer:
                answer = sum
        else:
            for i in range(col):
                if ch[i] == 0:
                    ch[i] = 1
                    dfs(L+1, sum + land[L][i])
                    ch[i] = 0
    dfs(0, 0)
    return answer

land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
land2 = [[1,1,1,1], [2,2,2,3], [3,3,3,6], [4,4,4,7]]
col = 4
print(solution(land2))