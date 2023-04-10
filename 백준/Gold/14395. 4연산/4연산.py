from collections import deque
s, t = map(int, input().split())
MAX = 10e9
def BFS():
    visited = set()
    q = deque()
    q.append((s, ''))
    operator = ['*', '+', '/']
    result = -1
    if s == t:
        return 0
    
    while q:
        node, op = q.popleft()
        
        if node == t:
            result = op
            break
        for o in operator:
            calc = eval(str(node) + o + str(node))
            if 0 <= node <= MAX and calc not in visited:
                q.append((calc, op+o))
                visited.add(calc)
    return result

print(BFS())