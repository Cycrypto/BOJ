import sys
input = sys.stdin.readline
print = sys.stdout.write
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split())
parent = [i for i in range(v)]
flag = False

cnt = 0
for i in range(e):
    cnt += 1
    a, b = map(int, input().split())
    if find(a) == find(b):
        flag = True
        break
    else:
        union(a, b)

print(str(cnt) if flag else "0")