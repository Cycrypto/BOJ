n = int(input())
outside = (n-1)* 4 + 1
graph = [[' ' for _ in range(outside)] for __ in range(outside)]
k = 0
flag = False
for i in range(outside//2 + 1):
    if i % 2 != 0:
        continue

    for j in range(k, len(graph)-k):
        graph[i][j] = '*'
        graph[outside-i - 1][j] = '*'
        graph[j][i] = '*'
        graph[j][outside-i-1] = '*'

    k += 2

for i in range(len(graph)):
    # print(graph[i])
    for j in range(len(graph[i])):
        print(graph[i][j], end='')
    print()