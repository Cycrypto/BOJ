import sys
input = sys.stdin.readline

def bi_sort(lst, start, end):
    while start <= end:
        mid = (start + end) // 2
        k= sum(map(lambda x: x//mid, lst))
        if k >= m:
            start = mid+1
        else:
            end = mid-1

    return end

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

print(bi_sort(lst, 1, lst[-1]))