n = int(input())

arr = list(map(int, input().split()))
dp = arr[:]
for i in range(n):   # 기준점
    for j in range(i):  # 검색
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))

