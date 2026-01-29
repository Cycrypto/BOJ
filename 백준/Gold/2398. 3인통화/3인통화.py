import sys
import heapq

input = sys.stdin.readline
INF = 10**18


def dijkstra(src, g, n):
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    dist[src] = 0
    parent[src] = src

    hq = [(0, src)]
    while hq:
        d, u = heapq.heappop(hq)
        if d != dist[u]:
            continue

        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(hq, (nd, v))

    return dist, parent


def collect_edges_on_path(parent, src, hub):
    edges = []
    cur = hub
    while cur != src:
        p = parent[cur]
        if p == -1:
            return []
        edges.append((cur, p))
        cur = p
    return edges


def main():
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    wmap = {}

    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
        if u > v:
            u, v = v, u
        wmap[(u, v)] = w

    a, b, c = map(int, input().split())

    da, pa = dijkstra(a, g, n)
    db, pb = dijkstra(b, g, n)
    dc, pc = dijkstra(c, g, n)

    hub = 1
    best = INF
    for x in range(1, n + 1):
        s = da[x] + db[x] + dc[x]
        if s < best:
            best = s
            hub = x

    used = set()
    for src, parent in ((a, pa), (b, pb), (c, pc)):
        for u, v in collect_edges_on_path(parent, src, hub):
            if u > v:
                u, v = v, u
            used.add((u, v))

    total_cost = sum(wmap[e] for e in used)

    edges = sorted(used)
    print(total_cost, len(edges))
    for u, v in edges:
        print(u, v)


if __name__ == "__main__":
    main()
