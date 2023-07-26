import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e8))
n, m = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for _ in range(100001)]
dp = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find(s):
    if dp[s] != -1:
        return dp[s]
    result = 1
    for ss in graph[s]:
        if height[ss] > height[s]:
            result = max(find(ss) + 1, result)
    dp[s] = result
    return dp[s]

for i in range(1, n+1):
    print(find(i))