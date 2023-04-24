import sys
input = sys.stdin.readline
print = sys.stdout.write
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

node, v = map(int, input().split())
v1, v2 = map(int, input().split())
parent = [i for i in range(node)]
graph = []

for i in range(v):
    a, b, weight = map(int, input().split())
    graph.append([a, b, weight])

graph.sort(key=lambda x: x[2], reverse=True)
result = 0
for g in graph:
    a, b, weight = g
    union(a, b)
    if find(v1) == find(v2):
        print(str(weight))
        break
