import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def check(dist, m, s):
    cnt = 0
    left = dist[0]
    for right in dist[1:]:
        if right - left >= m:
            cnt += 1
            left = right
    return cnt >= (s - 1)

def solve():
    _, s = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    left, right = 0, lst[-1]
    d = 0
    while left <= right:
        mid = (left + right) // 2
        if check(lst, mid, s):  # 콘센트를 꼽은 수가 많은 경우
            left = mid + 1
            d = max(d, mid)

        else:
            right = mid - 1
            
    print(d)

    
if __name__ == "__main__":
    for i in range(int(input())):
        solve()