import sys
input = sys.stdin.readline
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())
parent = [i for i in range(n+1)]

for i in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

answer = []
for i in range(1, n + 1):
    if i == parent[i]:
        answer.append(i)
print(*answer)