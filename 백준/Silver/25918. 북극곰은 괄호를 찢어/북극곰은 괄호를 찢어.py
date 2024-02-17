from collections import deque
n = int(input())
st = list(input())

q = deque([])
result = 0

for s in st:
    if not len(q) or s == q[-1]:
        q.append(s)
    
    else:
        q.pop()

    result = max(result, len(q))
print(result if len(q) == 0 else -1)