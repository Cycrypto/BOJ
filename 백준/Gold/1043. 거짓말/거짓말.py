import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())

parent = list(range(n + 1))

truth_line = list(map(int, input().split()))
t = truth_line[0]
truth_people = truth_line[1:]

parties = []
for _ in range(m):
    arr = list(map(int, input().split()))
    k = arr[0]
    people = arr[1:]
    parties.append(people)

    if k >= 2:
        base = people[0]
        for p in people[1:]:
            union(parent, base, p)

truth_roots = set(find(parent, p) for p in truth_people)

ans = 0
for people in parties:
    can_lie = True
    for p in people:
        if find(parent, p) in truth_roots:
            can_lie = False
            break
    if can_lie:
        ans += 1

print(ans)