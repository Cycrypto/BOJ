from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])
    maps[0][0] = 0
    visited[0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (0 <= nx < n and 0 <= ny < m ) and maps[nx][ny] != 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append([nx, ny])
                maps[nx][ny] = 0
    
    return (visited[n-1][m-1])
        
        