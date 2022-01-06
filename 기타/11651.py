axis = [list(map(int, input().split())) for _ in range(int(input()))]
axis.sort(key=lambda x: (x[1], x[0]))

for t in axis:
    print(*t)