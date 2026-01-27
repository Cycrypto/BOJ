import sys
import heapq

input = sys.stdin.readline
INF = 10**18

num_vertices, num_edges, start_vertex, target_vertex, budget = map(int, input().split())

adj_list = [[] for _ in range(num_vertices + 1)]
max_edge_cost = 0

for _ in range(num_edges):
    u, v, cost = map(int, input().split())
    adj_list[u].append((v, cost))
    adj_list[v].append((u, cost))
    if cost > max_edge_cost:
        max_edge_cost = cost


def can_reach_with_max_edge(max_allowed_edge_cost: int) -> bool:
    min_total_cost = [INF] * (num_vertices + 1)
    min_total_cost[start_vertex] = 0

    pq = [(0, start_vertex)]

    while pq:
        curr_total_cost, curr_vertex = heapq.heappop(pq)

        if curr_total_cost > min_total_cost[curr_vertex]:
            continue

        if curr_vertex == target_vertex:
            return curr_total_cost <= budget

        for next_vertex, edge_cost in adj_list[curr_vertex]:
            if edge_cost > max_allowed_edge_cost:
                continue

            next_total_cost = curr_total_cost + edge_cost
            if next_total_cost < min_total_cost[next_vertex] and next_total_cost <= budget:
                min_total_cost[next_vertex] = next_total_cost
                heapq.heappush(pq, (next_total_cost, next_vertex))

    return False


left, right = 0, max_edge_cost
answer = -1

while left <= right:
    mid = (left + right) // 2
    if can_reach_with_max_edge(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
