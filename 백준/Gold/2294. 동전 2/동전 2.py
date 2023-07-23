import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline
MAX = 9876543210
n, m = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0 for _ in range(m + 1)]

def find(N):
    if N == 0:
        return 0
    
    if dp[N] != 0:
        return dp[N]
    comp = MAX

    for c in coin:
        if N-c < 0: 
            continue

        s = find(N-c) + 1
        comp = comp if comp < s else s
    dp[N] = comp
    return dp[N]

result = find(m)
print(result if result != MAX else -1)