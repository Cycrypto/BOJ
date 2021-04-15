import sys
usr = int(input())
dp = [0 for _ in range (usr+1)]
for i in range (2, usr+1):
    dp[i] = dp[i-1] + 1
    if (i%2 == 0):
        if dp[i] < dp[int(i / 2)] + 1:
            dp[i] = dp[i]
        else:
            dp[i] = dp[int(i / 2)] + 1

    if (i % 3 == 0):
        if dp[i] < dp[int(i / 3)] + 1:
            dp[i] = dp[i]
        else:
            dp[i] = dp[int(i / 3)] + 1

print(dp[usr])