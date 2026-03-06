import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    row = list(map(int, input().split()))

    for j in range(i, 0, -1):
        if j == i:
            dp[j] = dp[j - 1] + row[j - 1]
        elif j == 1:
            dp[j] = dp[j] + row[j - 1]
        else:
            dp[j] = max(dp[j - 1], dp[j]) + row[j - 1]

print(max(dp))