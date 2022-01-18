n = int(input())
arr = list(map(int, input().split()))
dp1 = [1 for _ in range(1001)]
dp2 = [1 for _ in range(1001)]

for i in range(n):   # 기준점
    for j in range(i):  # 검색
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1, -1, -1):   # 기준점
    for j in range(i):  # 검색
        if arr[j] > arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)


print(max(list(map(sum, zip(dp1, dp2)))))

