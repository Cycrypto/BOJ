import sys
from itertools import accumulate

input = sys.stdin.readline

n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]
queries = [list(map(int, input().split())) for _ in range(m)]

gh = [list(accumulate(row)) for row in g]

out = []
for x1, y1, x2, y2 in queries:
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

    s = 0
    for i in range(x1, x2 + 1):
        if y1 == 0:
            s += gh[i][y2]
        else:
            s += gh[i][y2] - gh[i][y1 - 1]

    out.append(str(s))

print("\n".join(out))
