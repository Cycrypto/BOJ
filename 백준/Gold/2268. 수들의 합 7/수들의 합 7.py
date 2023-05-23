import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end):
    return prefix_sum(max(start, end)) - prefix_sum(min(start, end) - 1)


for i in range(m):
    f, a, b = map(int, input().split())
    if f == 0:  # sum() 함수 실행시
        print(interval_sum(a, b))

    else:   #modify() 함수 실행시
        update(a, (b - arr[a]))
        arr[a] = b
