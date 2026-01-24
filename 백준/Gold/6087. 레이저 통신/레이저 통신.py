import sys
import heapq

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
INF = 10 ** 18


def dijkstra_laser(grid, N, M, sx, sy, tx, ty):
    dist = [[[INF] * 4 for _ in range(M)] for _ in range(N)]
    pq = []
    
    for d in range(4):
        dist[sx][sy][d] = 0
        heapq.heappush(pq, (0, sx, sy, d))

    while pq:
        value, x, y, d = heapq.heappop(pq)

        if value != dist[x][y][d]:
            continue

        if x == tx and y == ty:
            return value

        for nd in range(4):
            nx, ny = x + dx[nd], y + dy[nd]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if grid[nx][ny] == '*':
                continue

            cost = 0 if nd == d else 1
            nv = value + cost

            if nv < dist[nx][ny][nd]:
                dist[nx][ny][nd] = nv
                heapq.heappush(pq, (nv, nx, ny, nd))

    return None


def main():
    M, N = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(N)]

    C = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'C':
                C.append((i, j))

    (sx, sy), (tx, ty) = C
    print(dijkstra_laser(grid, N, M, sx, sy, tx, ty))


if __name__ == "__main__":
    main()
