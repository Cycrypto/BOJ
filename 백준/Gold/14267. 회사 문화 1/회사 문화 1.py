import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
par = list(map(int, input().split()))

children = [[] for _ in range(n + 1)]
root = 1

for i in range(1, n + 1):
    p = par[i - 1]
    if p == -1:
        root = i
    else:
        children[p].append(i)

add = [0] * (n + 1)

for _ in range(m):
    s, lv = map(int, input().split())
    add[s] += lv


def dfs(u):
    for v in children[u]:
        add[v] += add[u]
        # print(add)
        dfs(v)


dfs(root)
print(*add[1:])
