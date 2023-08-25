from collections import deque
MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
reconsturct = [-1] * MAX

def solve(current):
    q = deque([current])
    visited[current] = 1
    while q:
        now = q.popleft()
        if now == k:
            return
        
        for c in [now * 2, now + 1, now - 1]:
            if 0 <= c < MAX and not visited[c]:
                q.append(c)
                visited[c] = visited[now] + 1
                reconsturct[c] = now

solve(n)
print(visited[k] - 1)

f = k
res = []
while f != -1:
    res.append(f)
    f = reconsturct[f]
print(*res[::-1])