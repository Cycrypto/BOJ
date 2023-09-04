def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x, y = find(x, parent), find(y, parent)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def solve():
    r, c = map(int, input().split())
    parent = [i for i in range(r*c+1)]
    graph = []

    for i in range(r):
        weight = list(map(int, input().split()))
        for j in range(c-1):
            node = i * c + j
            graph.append((weight[j], node, node+1))
    
    for i in range(r-1):
        weight = list(map(int, input().split()))
        for j in range(c):
            node = i * c + j
            graph.append((weight[j], node, node + c))
    
    graph.sort(key=lambda x: x[0])
    result = 0
    for e in graph:
        weight, a, b = e
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            result += weight
    
    return result
       

if __name__ == "__main__":
    for i in range(int(input())):
        print(solve())