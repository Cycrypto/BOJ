import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a > b:
        parent[a] = b
    
    else:
        parent[b] = a

def solve(t):
    user = int(input())
    connections = int(input())
    parent = [i for i in range(user+1)]  
  
    for _ in range(connections):
        union(*map(int, input().split()), parent)

    print(f"Scenario {t}:")
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(int(find(a, parent) == find(b, parent)))

if __name__ == "__main__":
    for i in range(int(input())):
        solve(i+1)
        print()