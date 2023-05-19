import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)])
left, right = 0, lst[-1]
result = 0

def check(mm):
    l = lst[0]
    cnt = 1

    for i in lst[1:]:
        if i - l >= mm:
            cnt += 1
            l = i

    return cnt >= m

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        result =  max(result, mid)
    else:
        right = mid - 1

print(result)
