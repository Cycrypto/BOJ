import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
INF = float('INF')
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * 3 for _ in range(n)]
cr = [*range(3)]

def solve(index, color):
    if index == n:
        return 0
    # print(house[index][color])
    if dp[index][color] != INF:
        return dp[index][color]
    
    for i in cr:
        if i != color:
            dp[index][color] = min(dp[index][color], house[index][color] + solve(index+1, i))
    return dp[index][color]

for i in cr:
    solve(0, i)

print(min(dp[0]))