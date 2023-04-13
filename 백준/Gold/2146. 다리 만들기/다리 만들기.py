from collections import deque
n = int(input())
result = 999
graph = [list(map(int, input().split())) for _ in range(n)]

continent_map = [[0 for _ in range(n)] for __ in range(n)]

def getContinent(x, y, mapped):
  visited = [[0 for _ in range(n)] for __ in range(n)]
  q = deque()
  q.append([x, y])
  visited[x][y] = 1
  graph[x][y] = mapped
  dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
  
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx = dx[i] + cx
      ny = dy[i] + cy

      if 0 <= nx < n and 0 <= ny < n:  # 범위안에 있을때
        if visited[nx][ny] == 0 and graph[nx][ny] != 0:
          graph[nx][ny] = mapped
          visited[nx][ny] = 1
          q.append([nx, ny])

m = 2
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:

      getContinent(i, j, m)  # 2부터 시작하는 숫자로 매핑
      m += 1


def buildBriedge(nn):
  global result
  visited = [[-1 for _ in range(n)] for __ in range(n)]
  q = deque()
  dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

  for i in range(n):
    for j in range(n):
      if graph[i][j] == nn:
        q.append([i, j])
        visited[i][j] = 0



  while q:
    cx, cy= q.popleft()
    for i in range(4):
      nx = dx[i] + cx
      ny = dy[i] + cy
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] > 0 and graph[nx][ny] != nn:
          result = min(result, visited[cx][cy])
          return

        if graph[nx][ny] == 0 and visited[nx][ny] == -1:
          visited[nx][ny] = visited[cx][cy] + 1
          q.append([nx, ny])



for i in range(2, m):
  buildBriedge(i)
  
print(result)