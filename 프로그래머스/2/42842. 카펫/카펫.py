from math import isqrt

def divisors(n):
    pairs = []
    r = isqrt(n)
    for d in range(1, r + 1):
        if n % d == 0:
            pairs.append((d, n // d))
    return pairs

def solution(brown, yellow):
    for h, w in divisors(yellow):
        if 2 * (w + h) + 4 == brown:
            W, H = w + 2, h + 2
            if W < H:
                W, H = H, W
            return [W, H]
