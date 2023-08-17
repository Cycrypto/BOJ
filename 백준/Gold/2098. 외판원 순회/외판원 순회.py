MAX = 20
INF = 1e9
n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1<<MAX)for _ in range(MAX)]

def shortestPath(here, visited):
    if visited == (1 << n) - 1:
        if dist[here][0] != 0:
            return dist[here][0]
        return INF
    
    if dp[here][visited] != -1:
        return dp[here][visited]
    
    dp[here][visited] = INF

    for nxt in range(n):
        if visited & (1 << nxt) or dist[here][nxt] == 0:
            continue
        dp[here][visited] = min(dp[here][visited], 
                                shortestPath(nxt, visited | (1 << nxt)) + dist[here][nxt])

    return dp[here][visited]

print(shortestPath(0, 1))