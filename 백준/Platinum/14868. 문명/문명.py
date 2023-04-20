import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

civ_q = deque()
bfs_q = deque()

n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for __ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
civil = [i for i in range(100001)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = i+1
    civ_q.append([x-1, y-1])



def bfs():
    while bfs_q:
        x,y = bfs_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n and 0 <= ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                civ_q.append((nx, ny))

def union_civ():
    global k
    while civ_q:
        x, y = civ_q.popleft()
        bfs_q.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 0:
                continue
            current = graph[x][y]
            nnext = graph[nx][ny]
            if (current == nnext) or is_same(current, nnext):
                continue
            union(current, nnext)
            k-=1


def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        civil[a] = b

def is_same(x, y):
    a = find(x)
    b = find(y)
    return a == b

def find(x):
    if civil[x] != x:
        civil[x] = find(civil[x])
    return civil[x]

year = 0
while k > 1:
    union_civ()
    if k == 1:
        print(str(year))
        break
    bfs()
    year+=1