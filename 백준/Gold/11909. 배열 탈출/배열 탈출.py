import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    for c in range(n):
        if 0>r-1 and 0>c-1:
            continue
        prev_r, prev_c = int(1e7), int(1e7)
        if 0<=r-1:
            prev_r = dp[r-1][c] + (0 if arr[r][c] < arr[r-1][c] else arr[r][c] - arr[r-1][c] + 1)
        if 0<=c-1:
            prev_c = dp[r][c-1] + (0 if arr[r][c] < arr[r][c-1] else arr[r][c] - arr[r][c-1] + 1)
        dp[r][c] = min(prev_r, prev_c)
print(dp[n-1][n-1])