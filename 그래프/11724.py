from collections import deque
def DFS(start, graph, visited):
    queue = [start]
    visited[start - 1] = True
    while queue:
        for i in graph[queue.pop()]:
            if not visited[i - 1]:
                visited[i - 1] = True
                queue.append(i)

    
if __name__ == "__main__":
    N, M = map(int, input().split())
    visited = [False for _ in range(N)]
    graph = {}
    for i in range (N):
        graph[i + 1] = set()

    for i in range(M):
        p, q = map(int, input().split())
        graph[p].add(q)
        graph[q].add(p)

    DFS(1, graph, visited)
    cnt = 1
    while True:
        try:
            DFS(visited.index(False) + 1, graph, visited)

            cnt += 1

        except Exception as e:
            break
    print (cnt)