N, M = list(map(int, input().split()))
ar = [*range(1, N + 1)]
for i in range(M):
    a, b = list(map(int, input().split()))
    t = ar[a - 1:b]
    ar[a-1:b] = t[::-1]
print(*ar)