import sys
sys.setrecursionlimit(int(1e6))
MAX = 1e6
arrow = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for __ in range(100001)]


def get_distance(fr, to):
    if fr == to:
        return 1
    
    if fr == 0:
        return 2
    
    fr -= 1; to -= 1
    if (fr+1) % 4 == to or (fr+3) % 4 == to:
        return 3
    
    if (fr+2) % 4 == to:
        return 4
    
    return MAX
    

def solve(index, right, left):
    if arrow[index] == 0:
        return 0
    
    if dp[index][right][left] != -1:
        return dp[index][right][left]

    dp[index][right][left] = min(solve(index + 1, arrow[index], left) + get_distance(right, arrow[index]), \
                                 solve(index + 1, right, arrow[index]) + get_distance(left, arrow[index]))
    
    return dp[index][right][left]

print(solve(0, 0, 0))
