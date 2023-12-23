import heapq
INF = float("INF")
t = int(input())

def solve(graph, attempt):
    q = []
    distance = [[INF] * t for _ in range(t)]
    heapq.heappush(q, (graph[0][0], 0, 0))
    
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while q:
        d, cx, cy = heapq.heappop(q)
        if cx == t - 1 and cy == t-1:
            print(f"Problem {attempt}:", distance[cx][cy])

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < t and 0 <= ny < t:
                nd = d + graph[nx][ny]
                if nd < distance[nx][ny]:
                    distance[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))

i = 1
while t:
    graph = [list(map(int, input().split())) for _ in range(t)]
    solve(graph, i)

    i += 1
    t = int(input())
