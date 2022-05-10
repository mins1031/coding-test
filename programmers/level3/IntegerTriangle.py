def solution(triangle):
    answer = 0
    dp = triangle[-1]

    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[0] += triangle[i-1][j]
            elif j == (len(triangle[i]) -1):
                dp[-1] += triangle[i-1][j-1]
            else:
                # if triangle[i-1][j-1] == triangle[i-1][j-1]:
                #     triangle[i-2][]
                # else:
                dp[j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(dp)

tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))