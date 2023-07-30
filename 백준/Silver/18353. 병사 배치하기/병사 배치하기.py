from bisect import bisect_left
n = int(input())
s = list(reversed(list(map(int, input().split()))))
lis = [int(1e9)]

for i in s:
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[bisect_left(lis, i)] = i

print(n- len(lis))