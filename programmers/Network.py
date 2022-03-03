def solution(n, computers):
    answer = 0
    ch = [0] * n
    net = [0] * n
    def dfs(L):
        nonlocal answer
        if L == n:
            for i in range(1, n):
                if net[i-1] == 1 and net[i] == 0:
                    answer += 1
        else:
            for i in range(n):
                if computers[L][i] == 1 and ch[i] == 0:
                    ch[i] = 1
                    net[i] = 1
                    dfs(L+1)
                    ch[i] = 0
    dfs(0)
    return answer

n = 3
computer1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computer2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computer2))
