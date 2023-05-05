import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)

i = 0
cnt = 0
while k:
    if k - lst[i] >= 0:
        k -=lst[i]
        cnt += 1
    else:
        i += 1
print(cnt)