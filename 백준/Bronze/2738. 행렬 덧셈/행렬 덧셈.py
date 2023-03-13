a, b = map(int, input().split())

lst = []
for _ in range(a):
    lst.append(list(map(int, input().split())))

for i in range(a):
    row = list(map(int, input().split()))
    for j in range(b):
        lst[i][j] += row[j]

for row in lst:
    print(*row)