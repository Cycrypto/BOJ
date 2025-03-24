from itertools import groupby
import sys

input = sys.stdin.readline

N,M,A,B = map(int, input().split())
T = list(map(int, input().split()))
like = set(map(int, input().split()))
hate = set(map(int, input().split()))

score = 0
prev = None
length = 0

for t in T:
    if t in like:
        cur = True
    elif t in hate:
        cur = False
    else:
        cur = None
    
    if cur == prev and cur is not None:
        length += 1
    else:
        if prev is not None and length >= 3:
            score += length if prev else -length
        length = 1 if cur is not None else 0
        prev = cur

if prev is not None and length >= 3:
    score += length if prev else -length

print(score)