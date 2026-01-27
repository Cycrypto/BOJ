import heapq

INF = float('inf')
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
min_total_cost = [INF] * (n+1)

for _ in range(m):
    u, v, cost = map(int, input().split())
    adj[u].append((v, cost))
    adj[v].append((u, cost))

start, end = map(int, input().split())
min_total_cost[start] = 0
pq = [(0, start)]

while pq:
    current_total_cost, current_v = heapq.heappop(pq)
    if current_total_cost > min_total_cost[current_v]:
        continue

    for next_v, next_cost in adj[current_v]:
        next_total_cost = current_total_cost + next_cost

        if next_total_cost < min_total_cost[next_v]:
            min_total_cost[next_v] = next_total_cost
            heapq.heappush(pq, (next_total_cost, next_v))

print(min_total_cost[end])