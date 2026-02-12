def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    puddles = set((x, y) for x, y in puddles)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) not in puddles or (i == 1 and j == 1):
                dp[i][j] = max(dp[i-1][j] + dp[i][j-1], dp[i][j]) % 1_000_000_007
                
    return dp[n][m]