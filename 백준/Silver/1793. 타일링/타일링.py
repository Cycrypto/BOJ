def tiling(n):
    if n == 0:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = tiling(n-1) + tiling(n-2)*2
    return dp[n]

while True:
    try:
        dp = [0] * 300
        dp[1], dp[2] = 1, 3
        print(tiling(int(input())))
    except:
        break