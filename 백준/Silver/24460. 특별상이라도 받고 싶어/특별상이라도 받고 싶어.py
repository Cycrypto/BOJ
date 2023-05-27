N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def conquer(x, y, n):
    if n == 1:
        return graph[x][y]
    div = n // 2
    lst = [
        conquer(x, y, div),
        conquer(x, y+div, div),
        conquer(x+div, y, div),
        conquer(x+div, y+div, div),
    ]
    return sorted(lst)[1]

print(conquer(0, 0, N))