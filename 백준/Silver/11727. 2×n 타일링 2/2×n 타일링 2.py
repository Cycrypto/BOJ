def tiling(n):
    if n == 0:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = (tiling(n-1) + tiling(n-2)*2) % 10007
    return dp[n]

dp = [0] * 1001
dp[1], dp[2] = 1, 3
print(tiling(int(input())))
