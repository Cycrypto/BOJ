from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

q = deque([[0, 0]])
visited[0][0] = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < n and 0 <= ny < m \
            and not visited[nx][ny] and graph[nx][ny]:
            q.append([nx, ny])
            visited[nx][ny] = visited[cx][cy] + 1

print(visited[n-1][m-1])