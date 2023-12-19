import heapq

INF = float('INF')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for to, d in graph[now]:
            cost = dist + d
            if cost < distance[to]:
                distance[to] = cost # 더 작은 값으로 교체
                heapq.heappush(q, (cost, to))

    return distance[N]


print(dijkstra(1))
