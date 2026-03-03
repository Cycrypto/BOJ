import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

Cmax = sum(cost)
dp = [0] * (Cmax + 1)

for m, c in zip(mem, cost):
    for total_c in range(Cmax, c - 1, -1):
        cand = dp[total_c - c] + m
        if cand > dp[total_c]:
            dp[total_c] = cand

for ans in range(Cmax + 1):
    if dp[ans] >= M:
        print(ans)
        break