import sys
sys.setrecursionlimit(int(1e9))
N, M = map(int,input().split())
mem = [[0] * N for _ in range(N)]

def pascal(n, m):
    if n == m or m == 0:
        return 1
    
    if m >= n:
        return 0
    
    if mem[n][m] != 0:
        return mem[n][m]
    else:
        mem[n][m] = pascal(n-1, m) + pascal(n-1, m-1)
        return mem[n][m]

print(pascal(N - 1, M - 1))