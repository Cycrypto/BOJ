import bisect

MIN = -9876543210

n = int(input())
lis = list(map(int, input().split()))
c = [MIN]

for i in range(n):
    if lis[i] > c[-1]:
        c.append(lis[i])
    
    else:
        c[bisect.bisect_left(c, lis[i])] = lis[i]
        
print(len(c) - 1)