n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(1001)]
sol = 1
for i in range(n):   # 기준점
    for j in range(i):  # 검색
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    sol = max(sol, dp[i])

print(sol)