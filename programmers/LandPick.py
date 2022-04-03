def solution(land):
    n = len(land)
    dp = [[0,0,0,0]] + land
    print(dp)

    for i in range(1, n+1):
        dp[i][0] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] += max(dp[i-1][1], dp[i-1][0], dp[i-1][3])
        dp[i][3] += max(dp[i-1][1], dp[i-1][2], dp[i-1][0])
    print(dp)
    return max(dp[n])

land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
land2 = [[1,1,1,1], [2,2,2,3], [3,3,3,6], [4,4,4,7]]
land3 = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
print(solution(land))
'''
결국 dp 테이블 만들고 계속 더한거임.... 하.... 개못한다 ㄹㅇ;;

'''