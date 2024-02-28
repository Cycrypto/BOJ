import sys
input = sys.stdin.readline

INF = float('INF')
m, n = map(int, input().split())
graph = [[INF] * (m+1) for _ in range(m+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a][b] = c

result = INF
for k in range(1, m + 1):
    for i in range(1, m + 1):
        for j in range(1, m+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        

for i in range(1, m+1):
    for j in range(1, m+1):        
        result = min(result, graph[i][i])

print(result if result != INF else -1)