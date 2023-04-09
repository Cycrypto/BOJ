from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

def in_range(x, y):
  return 0 <= x < n and 0 <= y < m

def BFS(x, y, graph):
  q = deque()
  q.append([x, y])
  graph[x][y] = 0

  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  cnt = 0
  while q:
    cx, cy = q.popleft()
    for i in range(4):
      nx, ny = cx + dx[i], cy + dy[i]
      if  in_range(nx, ny):
        if graph[nx][ny] == 1:
            q.append([nx, ny])
            graph[nx][ny] = 0
            cnt += 1
        else:
            continue

    # import pprint
    # pprint.pprint(graph)
  return cnt + 1


size = []
for x in range(len(graph)):
  for y in range(len(graph[x])):
    if graph[x][y]:
      size.append(BFS(x, y, graph))

if len(size):
    print(len(size))
    print(sorted(size)[-1])
else:
   print(0)
   print(0)