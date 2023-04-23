import sys
input = sys.stdin.readline
print = sys.stdout.write

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    result = 0
    #a, b, cost
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(N+1)]

    for edge in edges:
        a, b, cost = edge
        if find(a) != find(b):
            union(a, b)
            result += cost

    print(str(sum(list(zip(*edges))[2]) - result)+"\n")
