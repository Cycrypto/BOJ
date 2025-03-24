import sys
from itertools import groupby

input = sys.stdin.readline

N, M, A, B = map(int, input().split())
T = list(map(int, input().split()))
like = set(map(int, input().split()))
hate = set(map(int, input().split()))

mapped = [
    True if x in like else False if x in hate else None
    for x in T
]

score = 0

for key, group in groupby(mapped):
    if key == True or key == False:
        count = sum(1 for _ in group)
        if count >= 3:
            score += count if key else -count

print(score)