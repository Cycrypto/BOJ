def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
print = sys.stdout.write
n,m  = map(int, input().split())
parent = [i for i in range(n+1)]

for i in range(m):
    t, v, e = map(int, input().split())
    if t:
        if find_parent(parent, v) == find_parent(parent, e):
            print("YES\n")
        else:
            print("NO\n")
    else:
        union_parent(parent, v, e)