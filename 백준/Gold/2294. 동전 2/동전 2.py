import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000000)
 
def solve(K):
    if K == 0:
        return 0
    if memo[K] > 0:
        return memo[K]
 
    minVal = 999999
    for i in range(N):
        if K-coin[i] < 0:
            continue
        temp = solve(K-coin[i])+1
        if minVal > temp:
            minVal = temp
    memo[K] = minVal
    return minVal
 
N, K = map(int, read().split())
coin = []
memo = [0 for _ in range(K+1)]
for _ in range(N):
    coin.append(int(read()))
 
ans = solve(K)
if ans == 999999:
    print(-1)
else:
    print(ans)