from collections import deque
def solution(s):
    s = deque(list(s))
    q = deque([])
    while s:
        cur = s.popleft()
        if cur == '(':
            q.append(cur)
            
        else:
            if len(q) and q[-1] == '(':
                q.pop()
            else:
                q.append(cur)
                
    return not(len(q))