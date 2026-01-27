import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

tc = int(input())


def solve():
    computer, dependency, hacked_computer = map(int, input().split())
    network_map = [[] for _ in range(computer + 1)]
    adj = [INF] * (computer + 1)
    adj[hacked_computer] = 0

    for _ in range(dependency):
        n, v, t = map(int, input().split())
        network_map[v].append((n, t))

    pq = [(0, hacked_computer)]
    while pq:
        cur_dist, cur_com = heapq.heappop(pq)
        if cur_dist > adj[cur_com]:
            continue

        for nv, nt in network_map[cur_com]:
            next_dist = cur_dist + nt
            if next_dist < adj[nv]:
                adj[nv] = next_dist
                heapq.heappush(pq, (next_dist, nv))

    print(len(adj) - adj.count(INF), max(filter(lambda x: x != INF, adj)))


for _ in range(tc):
    solve()
