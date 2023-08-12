INF = 1001
n, m = map(int, input().split())
if m == 0:
    print(0)
    exit()

caffain = list(map(int, input().split()))
dp = [[-1]*(101) for _ in range(100001)]

def solve(k, idx):
    if k- caffain[idx] == 0:
        return 1
    
    if idx == n-1:
        return INF
    
    if dp[k][idx] != -1:
        return dp[k][idx]
    
    dp[k][idx] = min(solve(k-caffain[idx], idx+1) + 1, solve(k, idx+1))
    return dp[k][idx]

result = solve(m, 0)
print(result if result != INF else -1)