def solution(triangle):
    scaled_triangle = [sub + [0] * (len(triangle) - len(sub)) for sub in triangle]
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = scaled_triangle[0][0]
    for i in range(1, len(scaled_triangle)):
        for j in range(len(scaled_triangle[i])):
            if j-1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + scaled_triangle[i][j])
            dp[i][j] = max(dp[i][j], dp[i-1][j] + scaled_triangle[i][j])
    return max(dp[-1])