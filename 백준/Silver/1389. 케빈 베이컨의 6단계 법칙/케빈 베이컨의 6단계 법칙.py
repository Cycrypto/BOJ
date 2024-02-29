INF = float("INF")
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[k][j] + graph[i][k])

result = []
for s in graph[1:]:
    result.append(sum(s[1:]))
print(result.index(min(result)) + 1)