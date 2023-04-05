result = []
def dfs(graph, visited, s):
    global result
    visited[s] = True
    result.append(s)
    for i in graph[s - 1]:
        if not visited[i]:
            dfs(graph, visited, i)
    return result

def initGraph(N):
    graph = [[] for _ in range(N + 1)]
    for i in range(N):
        graph[i].append(int(input()))
    return graph

N = int(input())
graph = initGraph(N)
m_len = 0
solve = 0

for i in range(N):
    visited = [False for _ in range(N + 1)]
    res = dfs(graph, visited, i)

    if m_len < len(res):
        solve = i
        m_len = len(res)
    result = []
print(solve)
    