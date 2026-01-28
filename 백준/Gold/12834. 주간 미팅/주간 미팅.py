import sys, heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(s, g):
    hq = [(0, s)]
    dist = [INF] * (len(g))
    dist[s] = 0

    while hq:
        current_dist, current_vertex = heapq.heappop(hq)
        if current_dist > dist[current_vertex]:
            continue

        for n_vertex, n_dist in g[current_vertex]:
            next_dist = current_dist + n_dist
            if next_dist < dist[n_vertex]:
                dist[n_vertex] = next_dist
                heapq.heappush(hq, (next_dist, n_vertex))

    dist = [-1 if d == INF else d for d in dist]

    return dist


def main():
    n, v, e = map(int, input().split())
    a, b = map(int, input().split())
    member_position = list(map(int, input().split()))
    g = [[] for _ in range(v+1)]

    for _ in range(e):
        i, j, k = map(int, input().split())
        g[i].append((j,k))
        g[j].append((i, k))

    result = 0
    for m in member_position:
        res = dijkstra(m, g)
        result += (res[a] + res[b])

    print(result)

main()
