import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if cost[a] <= cost[b]:
        parent[b] = a
    else:
        parent[a] = b
n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = [i for i in range(n)]

for i in range(m):
    v, e = map(int, input().split())
    union(parent, v - 1, e - 1)

result = 0
for i, r in enumerate(parent):
    if i == r:
        result += cost[i]

if result <= k:
    print(result)  
else:
    print("Oh no")