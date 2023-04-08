import pprint
graph = []
visited = [[False for _ in range(5)] for __ in range(5)]
flag = False
for i in range(5):
    graph.append(list(map(int, input().split())))

n, m = map(int, input().split())

def BFS(x, y, apple, depth = 0):
    global flag
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if (depth <= 3 and apple >= 2):
        flag = True
        return
    
    if (depth >= 3 and apple < 2):
        return
    
    for i in range(4):

        xx = dx[i] + x
        yy = dy[i] + y
        if 0 <= xx < 5 and 0 <= yy < 5:
            if graph[xx][yy] == 0 and visited[xx][yy] == False:
                BFS(xx, yy, apple, depth + 1)
        
            elif graph[xx][yy] == 1 and visited[xx][yy] == False:
                BFS(xx, yy, apple + 1, depth + 1)
            
            else:
                continue
        
            visited[xx][yy] = False
    
    if depth == 0:
        if flag:
            return 1
        return 0

    

print(int(BFS(n, m, 0)))
