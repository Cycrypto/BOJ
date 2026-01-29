import sys, heapq

INF = float('INF')
input = sys.stdin.readline


def dijkstra(g, start, end, blocked=None):
    distance = [INF] * (end + 1)
    distance[start] = 0

    prev = [-1] * (end + 1)
    hq = [(0, start)]

    while hq:
        curr_dist, curr_vertex = heapq.heappop(hq)
        if curr_dist > distance[curr_vertex]:
            continue

        for nv, nd in g[curr_vertex]:
            if blocked is not None:
                a, b = blocked
                if (curr_vertex == a and nv == b) or (curr_vertex == b and nv == a):
                    continue

            next_dist = curr_dist + nd
            if distance[nv] > next_dist:
                distance[nv] = next_dist
                prev[nv] = curr_vertex
                heapq.heappush(hq, (next_dist, nv))

    return distance, prev


def restore_path(prev, s, t):
    path = []
    cur = t

    while cur != -1:
        path.append(cur)
        if cur == s:
            break
        cur = prev[cur]

    if not path or path[-1] != s:
        return None

    path.reverse()
    return path


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))

    shortest_dist, prev = dijkstra(g, 1, n)
    base = shortest_dist[n]
    if base == INF:
        print(-1)
        return

    path = restore_path(prev, 1, n)
    if path is None:
        print(-1)
        return

    ans = 0
    for i in range(len(path) - 1):
        blocked = (path[i], path[i+1])
        dist2, _ = dijkstra(g, 1, n, blocked=blocked)

        if dist2[n] == INF:
            print(-1)
            return

        ans = max(ans, dist2[n] - base)

    print(ans)


if __name__ == "__main__":
    main()
