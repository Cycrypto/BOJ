import sys
input = sys.stdin.readline
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


lecture, connection = map(int, input().split())
parent = [i for i in range(lecture+1)]

for i in range(connection):
    union(*map(int, input().split()))

cnt = 0
timetable = list(map(int, input().split()))
current = timetable[0]
for i in timetable[1:]:
    if find(current) != find(i):
        cnt += 1
        current = i
print(cnt)