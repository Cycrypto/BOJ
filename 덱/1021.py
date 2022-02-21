from collections import deque
N, M = map(int, input().split())
deq = deque([1, 2])

for i in range(N-M):
    deq.append(0)
lst = list(map(int, input().split()))
for j in lst:
    deq.appendleft(j)

print(deq)