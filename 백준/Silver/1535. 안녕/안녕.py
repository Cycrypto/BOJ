n, k = int(input()), 99
L = list(map(int, input().split())) # 무게
J = list(map(int, input().split())) # 가치

items = [(0, 0)] + [(w, v) for w, v in zip(L, J)]
dp = [[0] * (k+1) for _ in range(n+1)]
r = 0

for i in range(1, n + 1):
    current_weight, current_value = items[i]
    for j in range(k + 1):
        if current_weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j - current_weight] + current_value
            )
    r = max(r, max(dp[i]))
print(r)