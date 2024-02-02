from collections import defaultdict
parent = [i for i in range(201)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
        

def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):          
            if computers[i][j] == 1:
                union(i, j)
    
        di = defaultdict(int)
    for i in parent[:n]:
        di[find(i)] += 1

    return len(di.items())
