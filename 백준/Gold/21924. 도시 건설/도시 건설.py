import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        parent[x] = y

    else:
        parent[y] = x

n, m = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]
#a, b, cost
graph.sort(key=lambda x: x[2])
mmax = sum(list(zip(*graph))[2])

res = 0
for a, b, cost in graph:
    if find(a) != find(b):
        union(a, b)
        res += cost

tmp = 0
for i in range(1, n+1):
    if parent[i] == i:
        tmp += 1

print(mmax - res if tmp == 1 else -1)