def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    parent = [i for i in range(n+1)]

    def find(x):
        nonlocal parent
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        nonlocal parent
        x = find(x)
        y = find(y)
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    for i, s in enumerate(lst):
        union(s, i+1)
    
    for i in lst:
        find(i)
    
    print(len(set(parent)) - 1)

if __name__ =="__main__":
    for _ in range(int(input())):
        solve()