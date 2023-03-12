N, M = map(int, input().split())
ar = [0] * N

for i in range(M):
    a, b, c = map(int, input().split())
    ar[a - 1: b] = [c] * (b - a + 1)
print(*ar)