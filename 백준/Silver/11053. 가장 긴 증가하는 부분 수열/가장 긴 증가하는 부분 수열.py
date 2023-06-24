n = int(input())
lst = list(map(int, input().split()))


dp = [-1 for _ in range(1001)]
def lis_dp(start):
    if dp[start] != -1:
        return dp[start]
    dp[start] = 1
    for i in range(start+1, n):
        if (lst[start] < lst[i]):
            dp[start] =  max(dp[start], lis_dp(i)+1)
    return dp[start]

max_len = 0
for i in range(n):
    max_len = max(max_len, lis_dp(i))
print(max_len)