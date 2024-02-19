from collections import deque
x, y = map(int, input().split())
maps = [list(input()) for _ in range(x)]
visited = [[0] * y for _ in range(x)]


def bfs(x, y):
    global maps, visited
    q = deque([[x, y]])
    visited[x][y] = 1
    count_sheep, count_wolf = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(visited) and 0 <= ny < len(visited[0]):
                if visited[nx][ny] != 0 or maps[nx][ny] == '#':
                    continue

                if maps[nx][ny] == 'o':
                    count_sheep += 1
                
                if maps[nx][ny] == 'v':
                    count_wolf += 1
                
                visited[nx][ny] = 1
                q.append([nx, ny])
    if count_sheep > count_wolf:
        return count_sheep, 0
    
    else:
        return 0, count_wolf

result_sheep, result_wolf = 0, 0
for i in range(x):
    for j in range(y):
        if maps[i][j] != '#' or not visited[i][j]:
            s, w = bfs(i, j)
            result_sheep += s
            result_wolf += w

print(result_sheep, result_wolf)
