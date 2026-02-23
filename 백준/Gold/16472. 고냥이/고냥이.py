import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
meow = list(input().strip())

left = 0
ans = 0

cnt = Counter()
distinct = 0

for right in range(len(meow)):
    ch = meow[right]
    if cnt[ch] == 0:
        distinct += 1
    cnt[ch] += 1

    while distinct > n:
        c = meow[left]
        cnt[c] -= 1
        if cnt[c] == 0:
            distinct -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)