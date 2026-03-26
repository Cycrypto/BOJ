from collections import deque


n, L = map(int, input().split())
s = list(map(int, input().split()))

dq = deque()
result = []

for i, x in enumerate(s):
    while dq and dq[0] <= i - L:
        dq.popleft()
    while dq and s[dq[-1]] >= x:
        dq.pop()
    dq.append(i)

    result.append(s[dq[0]])
print(*result)