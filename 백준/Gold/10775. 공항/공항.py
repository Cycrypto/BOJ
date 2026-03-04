import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


g = int(input())
p = int(input())

parent = list(range(g + 1))

answer = 0

for _ in range(p):
    g = int(input())
    gate = find(parent, g)
    if gate == 0:
        break

    union(parent, gate, gate - 1)
    answer += 1
print(answer
      )