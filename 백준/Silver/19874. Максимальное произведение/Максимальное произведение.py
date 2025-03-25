import itertools

n = int(input())
l = list(map(int, input().split()))
s = list(itertools.accumulate(l))

result = -1
ans = 0
for i in range(n-1):
    if (k:=s[i] * (s[-1] - s[i])) > result:
        result = k
        ans = i + 1
print(ans)