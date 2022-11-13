tc = int(input())
for _ in range(tc):
    k = int(input())
    n = int(input())

    apart = [[] for i in range(k + 1)]
    apart[0] = [i + 1 for i in range(n)]

    for i in range(1, k + 1):
        s = 0
        for j in range(n):
            s += apart[i - 1][j]
            apart[i].append(s)

    print(apart[k][n - 1])