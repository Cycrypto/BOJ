val = int(input())//2

start, end = 0, val // 2
calc = lambda n: (n * (n-1)) // 2
while start <= end:
    mid = (start + end) // 2
    if calc(mid) < val:
        start = mid + 1
    else:
        end = mid - 1
print(end)