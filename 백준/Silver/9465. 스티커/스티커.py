import sys
input = sys.stdin.readline

tc = int(input().strip())
for _ in range(tc):
    k = int(input().strip())
    s = [list(map(int, input().split())) for _ in range(2)]

    if k == 1:
        print(max(s[0][0], s[1][0]))
        continue

    dp = [[0] * k for _ in range(2)]
    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]
    dp[0][1] = s[0][1] + dp[1][0]
    dp[1][1] = s[1][1] + dp[0][0]

    for j in range(2, k):
        dp[0][j] = s[0][j] + max(dp[1][j-1], dp[1][j-2])
        dp[1][j] = s[1][j] + max(dp[0][j-1], dp[0][j-2])

    print(max(dp[0][k-1], dp[1][k-1]))
