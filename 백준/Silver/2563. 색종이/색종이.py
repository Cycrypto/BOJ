grid = [[0 for i in range(100)] for j in range(100)]

for i in range(int(input())):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            grid[j][k] = 1

area = 0
for row in grid:
    area += sum(row)

print(area)