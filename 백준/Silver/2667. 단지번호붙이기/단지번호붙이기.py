n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
def DFS(x, y):
    graph[x][y] = 0
    res = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y

        if 0 <= xx < len(graph) and 0 <= yy < len(graph):
            if graph[xx][yy] == 1:
                res += (DFS(xx, yy) + 1)   
    return res

result = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            result.append(DFS(i, j) + 1)

result.sort()
print(len(result))
for i in result:
    print(i)