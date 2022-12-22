input()
A = list(map(int, input().split()))

mini = A[0]
dp = [0] * len(A)

for i in range(1, len(A)):
    dp[i] = max(dp[i - 1], A[i] - mini)
    mini = min(mini, A[i])

print(*dp)