from collections import defaultdict, deque

def solution(n, wires):
    graphs = defaultdict(set)
    result = float('INF')
        
    for s, e in wires:
        graphs[s].add(e)
        graphs[e].add(s)
        
    def bfs(s):
        q = deque([s])
        visited = [False] * (n + 1)
        visited[s] = True
        cnt = 1
        
        while q:
            x = q.popleft()
            for nx in graphs[x]:
                if not visited[nx]:
                    visited[nx] = True
                    cnt += 1
                    q.append(nx)
        return cnt
        
    for cs, ce in wires:
        graphs[cs].remove(ce)
        graphs[ce].remove(cs)
        
        result = min(result, abs(bfs(cs) - bfs(ce)))
        
        graphs[cs].add(ce)
        graphs[ce].add(cs)
    return result
        