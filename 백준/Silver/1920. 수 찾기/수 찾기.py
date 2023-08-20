from bisect import bisect_left, bisect_right
n = int(input())
lst = sorted(list(map(int, input().split())))
m = int(input())
lst2 = list(map(int, input().split()))

for i in lst2:
    if bisect_right(lst, i) - bisect_left(lst, i):
        print(1)
    else:
        print(0)