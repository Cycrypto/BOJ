import sys
import heapq
INF = float('INF')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for  _ in range(n+1)]
transit = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            continue

        for to, co in graph[now]:
            cost = dist + co
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(q, (cost, to))
                transit[to] = now

    # print(transit)    
    result = ['-'] * (n)
    for i in range(n):
        if i+1 == start:
            continue

        temp = i+1
        while transit[temp] != start:
            temp = transit[temp]
        result[i] = temp            

    print(*result)

for i in range(1, n+1):
    dijkstra(i)
