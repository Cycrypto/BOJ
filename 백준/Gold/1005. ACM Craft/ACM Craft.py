import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    to_win = int(input())

    dp = [-1] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            dp[i] = cost[i]
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + cost[i])
            if not indegree[i]:
                q.append(i)
    # print(dp)
    print(dp[to_win])
        

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()