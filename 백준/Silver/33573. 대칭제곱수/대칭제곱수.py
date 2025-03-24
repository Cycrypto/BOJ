from math import isqrt
import sys
input = sys.stdin.readline

def is_super_square(n_str):
    n = int(n_str)
    r = int(n_str[::-1].lstrip('0'))

    sqrt_n = isqrt(n)
    sqrt_r = isqrt(r)

    return sqrt_n * sqrt_n == n and sqrt_r * sqrt_r == r

T = int(input())
for _ in range(T):
    N = input().strip()
    print("YES" if is_super_square(N) else "NO")