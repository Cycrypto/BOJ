import sys
from collections import Counter

input = sys.stdin.readline
N = int(input().strip())
cards = Counter(list(map(int, input().split())))

M = int(input().strip())
queries = list(map(int, input().split()))

result = []
for q in queries:
    result.append(str(cards.get(q, 0)))
print(" ".join(result))
