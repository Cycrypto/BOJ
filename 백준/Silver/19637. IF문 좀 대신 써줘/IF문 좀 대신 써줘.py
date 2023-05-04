import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = []

def bi_search(target):
    start, end = 0, n
    while start <= end:
        mid = (start + end) // 2
        if target > lst[mid][1]:
            start = mid + 1
        else:
            end = mid - 1  

    return(lst[start][0])

for i in range(n):
    a, b = input().split()
    lst.append([a, int(b)])

for j in range(m):
   print(bi_search(int(input())))
