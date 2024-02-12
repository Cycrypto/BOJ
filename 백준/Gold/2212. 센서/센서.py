n = int(input())
m = int(input())
lst = list(map(int, input().split()))
lst.sort()
dist = [lst[i] - lst[i-1] for i in range(1, n)]

print(sum(sorted(dist)[:len(lst) - m]))