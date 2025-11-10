from math import ceil

s = input().strip()

cnt = [0]*10
for ch in s:
    cnt[int(ch)] += 1

cnt[6] = (cnt[6] + cnt[9] + 1) // 2
cnt[9] = 0

print(max(cnt))