import math
from collections import Counter
n = int(input())
arr = [int(input()) for _ in range(n)]

print(math.floor(sum(arr) / len(arr)))
print(sorted(arr)[int(len(arr)/2)])
arr.sort()
cnt = Counter(arr).most_common(2)

if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

else:
    print(cnt[0][0])

print(max(arr) - min(arr))

