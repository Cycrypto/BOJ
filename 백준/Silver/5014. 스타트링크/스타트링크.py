import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

distance = [-1] * (f + 1)
distance[s] = 0


q = deque([s])

while q:
    n = q.popleft()
    mv = [n + u, n - d]
    if n == g:
        break

    for m in mv:
        if 1 <= m <= f and distance[m] == -1:
            distance[m] = distance[n] + 1
            q.append(m)

print(distance[g] if distance[g] != -1 else "use the stairs")