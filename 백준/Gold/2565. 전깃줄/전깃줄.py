from bisect import bisect_left
n = int(input())
connection = [list(map(int, input().split())) for _ in range(n)]
connection.sort(key=lambda x: x[0])
dp = [-float('INF')]
for _, i in connection:
    if i < dp[-1]:
        dp[bisect_left(dp, i)] = i
    else:
        dp.append(i)

print(n - len(dp) + 1)