from bisect import bisect_right, bisect_left

n = int(input())
s = sorted(list(map(int, input().split())))
m = int(input())
k = list(map(int, input().split()))

for t in k:
    u = bisect_left(s, t)
    if u in range(n) and t == s[u]:
        print(1, end=' ')
        continue
    print(0, end=' ')
