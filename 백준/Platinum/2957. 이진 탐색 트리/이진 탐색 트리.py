from bisect import bisect_left, insort_left
import sys
input = sys.stdin.readline
print = sys.stdout.write
print('0\n')
tc = int(input())
M = dict()
M[int(input())] = 0
cnt = 0

for i in range(tc - 1):
    k = list(set(M.keys()))
    val = int(input())
    lower = bisect_left(k, val)
    cmp1, cmp2 = 0, 0
    
    if lower < len(k):
        cmp1 = M[k[lower]]
    
    if 0 < lower:
        lower -= 1
        cmp2 = M[k[lower]]

    M[val] = max(cmp1, cmp2) + 1
    cnt += max(cmp1, cmp2) + 1
    print(str(cnt)+"\n")
