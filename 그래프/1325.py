from sys import stdin
from collections import deque

read = stdin.readline

def BFS(start, dic):
    cnt = 0
    queue = deque()
    queue.appendleft(start)
    visited = []
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.appendleft(i)
                cnt += 1

    return cnt

dic = {}
N, M = map(int, read().split())
for i in range (N):
   dic[i + 1] = set()

for i in range (M):
    a, b = map(int, read().split())
    dic[b].add(a)
result = []
ans = 0

for i in range(1, N + 1):
    n = BFS(i, dic)
    if ans < n:
        ans = n
        result = [i]

    elif ans == n:
        result.append(i)

print(*result)