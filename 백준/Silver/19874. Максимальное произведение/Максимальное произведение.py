int(input())
l = list(map(int, input().split()))
result = -1
ans = 0
for i in range(len(l)):
    if (k:=sum(l[:i+1]) * sum(l[i+1:])) > result:
        result = k
        ans = i + 1
print(ans)