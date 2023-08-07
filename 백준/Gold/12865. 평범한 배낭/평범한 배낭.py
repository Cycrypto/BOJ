n, k = map(int, input().split())
we = []
va = []
dp = [[-1]*101 for _ in range(100001)]

for i in range(n):
    weight, value = map(int, input().split())
    we.append(weight);   va.append(value)


def pack(capacity, item):
    if (item == n):
        return 0

    if dp[capacity][item] != -1:
        return dp[capacity][item]

    dp[capacity][item] = pack(capacity, item+1)

    if capacity >= we[item]:
        dp[capacity][item] = max(dp[capacity][item], pack(capacity-we[item], item+1) + va[item])
    
    return dp[capacity][item]

print(pack(k, 0))
