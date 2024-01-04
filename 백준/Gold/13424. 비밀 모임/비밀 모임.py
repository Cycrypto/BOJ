import sys
import heapq
INF = float('INF')
# input = sys.stdin.readline().rstrip

tc = int(input())
def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    int(input())
    room_list = list(map(int, input().split()))
    dist_res = None
    for r in room_list:
        res = dijkstra(n, graph, r)
        if dist_res == None:
            dist_res = res
            continue
        dist_res = list(map(sum, zip(dist_res, res)))
    
    print(dist_res.index(min(dist_res)))
    
    
def dijkstra(n, graph, start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for to, co in graph[now]:
            cost = dist + co
            if distance[to] > cost:
                distance[to] = cost
                heapq.heappush(q, (cost, to))
    
    return distance

for _ in range(tc):
    solve()