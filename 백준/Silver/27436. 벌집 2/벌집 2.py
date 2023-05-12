N = int(input())
start, end = 1, 100000000000001
calc = lambda x: 3 * x * (x - 1) + 1

while start <= end:
    mid = (start + end) // 2
    if calc(mid) >= N:
        end = mid - 1
        temp = mid
 
    else:
        start = mid + 1
print(int(temp))