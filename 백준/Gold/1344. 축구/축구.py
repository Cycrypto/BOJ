PART = 18
pa = int(input())*0.01
pb = int(input())*0.01

nprime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

dp = [[0] * (PART+1) for _ in range(PART+1)]

def binom(n, m):
    if n == m or m == 0:
        return 1
    
    if m >= n:
        return 0
    
    if dp[n][m] != 0:
        return dp[n][m]
    else:
        dp[n][m] = binom(n-1, m) + binom(n-1, m-1)
        return dp[n][m]

res = 0
aa, bb = 0, 0
for r in nprime:
    aa += binom(18, r) * (pa**r) *  ((1-pa)**(PART - r))
    bb += binom(18, r) * (pb**r) *  ((1-pb)**(PART - r))

print(1-aa*bb)
