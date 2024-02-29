import sys
input = sys.stdin.readline

INF = float('INF')
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[k][j] + graph[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j] if graph[i][j] != INF else '0', end=' ')
    print()