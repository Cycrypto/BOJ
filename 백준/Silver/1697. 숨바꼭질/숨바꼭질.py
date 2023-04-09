from collections import deque
a, b = map(int, input().split())
line = [0] * ((10**5) + 1)

q = deque()
q.append(a)
cnt = 0
while q:
    cx = q.popleft()
    if cx == b:
        print(line[cx])
        break
    
    for nx in [cx-1, cx+1, 2*cx]:
        if 0 <= nx <= (10**5) and not line[nx]:
            line[nx] = line[cx] + 1
            q.append(nx)
