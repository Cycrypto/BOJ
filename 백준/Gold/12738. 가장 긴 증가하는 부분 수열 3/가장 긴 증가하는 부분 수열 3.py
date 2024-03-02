n = int(input())
lst = list(map(int, input().split()))
dp = [-1] * (n+1)


def lis(start):
    if dp[start] != -1:
        return dp[start]
    
    dp[start] = 1
    for i in range(start+1, n):
        if lst[start] < lst[i]:
            dp[start] = max(dp[start], lis(i) + 1)

    return dp[start]

from bisect import bisect_left
def lis_nlogn():
    MIN = -float('INF')
    lst_lis = [MIN]
    for i in lst:
        if i > lst_lis[-1]:
            lst_lis.append(i)
        else:
            lst_lis[bisect_left(lst_lis, i)] = i

    return lst_lis

print(len(lis_nlogn()) - 1)