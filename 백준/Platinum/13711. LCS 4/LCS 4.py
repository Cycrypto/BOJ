import sys
import bisect
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

da = dict().fromkeys([i for i in range(n + 1)], -1)
db = dict().fromkeys([i for i in range(n + 1)], -1)

for i in range(n):
    da[A[i]] = i
    db[B[i]] = i

C = []
for i in range(n):
    C.append(db[A[i]])
    
lis = [-float("INF")]
for c in C:
    if c > lis[-1]:
        lis.append(c)
    else:
        lis[bisect.bisect_left(lis, c)] = c
print(len(lis) - 1)
