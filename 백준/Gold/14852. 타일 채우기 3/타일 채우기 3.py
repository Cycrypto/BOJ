import sys
sys.setrecursionlimit(int(1e6))
n = int(input())
dp = [0] * int(1e7)
dp[0], dp[1], dp[2] = 1, 2, 7

def tiling(n):
    if dp[n] != 0:
        return dp[n]
    
    else:
        dp[n] = (tiling(n-1)*3 + tiling(n-2) - tiling(n-3)) % 1000000007
    return dp[n]

print(tiling(n))