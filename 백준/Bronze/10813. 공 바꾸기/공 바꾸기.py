N, M = map(int, input().split())
ar = [i for i in range(1, N + 1)]
for j in range(M):
    a, b = map(int, input().split())
    ar[a - 1], ar[b - 1] = ar[b - 1], ar[a - 1]
print(*ar)