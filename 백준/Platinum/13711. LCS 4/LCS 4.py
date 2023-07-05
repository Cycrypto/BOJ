import sys
import bisect
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [-1]*n
for idx, a in enumerate(A):
    C[idx] = B.index(A[idx])

lis = [-float("INF")]
for c in C:
    if c > lis[-1]:
        lis.append(c)
    else:
        lis[bisect.bisect_left(lis, c)] = c
print(len(lis) - 1)
