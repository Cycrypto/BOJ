import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i+1:[] for i in range(n)}
water = [0] * (n+1); water[1] = 100
result = 0

for i in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)

for i in range(1, n+1):
    for j in graph[i]:
        water[j] += water[i] / len(graph[i])

for i in range(1, n+1):
    if len(graph[i]) == 0:
        result = max(result, water[i])

print(result)