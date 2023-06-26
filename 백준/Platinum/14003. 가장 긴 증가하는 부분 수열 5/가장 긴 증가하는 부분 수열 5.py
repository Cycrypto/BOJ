from bisect import bisect_left
n = int(input())
s = list(map(int, input().split()))
c = [-float('INF')]
dp = [0] * (n)

for i in range(n):
    if c[-1] < s[i]:
        c.append(s[i])
        dp[i] = len(c) - 1
    else:
        c[k:=bisect_left(c, s[i])] = s[i]
        dp[i] = k

size, res = len(c) -1, []
for i in range(n-1, -1, -1):
    if dp[i] == size:
        res.append(s[i])
        size -= 1
print(len(c) - 1)
print(*res[::-1])