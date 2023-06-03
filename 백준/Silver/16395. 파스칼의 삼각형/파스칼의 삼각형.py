N, M = map(int,input().split())
pascal = [[1 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
print(pascal[N-1][M-1])