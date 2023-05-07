import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [int(input())for _ in range(n)]
lst.sort()
start, end = 0, max(lst)*m
result = end
while start <= end:
    mid = (start + end) // 2
    if (sum(list(map(lambda x: mid // x, lst)))) >= m:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
print(result)