import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

i = 0
cnt = 0
for op in lst:
    if k == 0:
        break
    if k >= op:
        m = k // op
        k -= (m*op)
        cnt += m
print(cnt)