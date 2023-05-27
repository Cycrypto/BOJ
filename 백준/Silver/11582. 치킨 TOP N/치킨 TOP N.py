import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
step = int(input())
size = n // step    # 8 // 2 == 4
start, end = 0, size
result = []
while end <= len(lst):
    result.append(sorted(lst[start:end]))
    start = end
    end += size
print(*sum(result, []))