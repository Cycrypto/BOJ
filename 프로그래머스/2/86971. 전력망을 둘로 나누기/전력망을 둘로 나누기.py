from collections import Counter
INF = float('INF')

def solution(n, wires):
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
        return parent
        
    minimum = INF
    for i in range(n):
        parent = [i for i in range(n+1)]
        for j in range(n-1):
            if j == i:
                continue
            union(wires[j][0], wires[j][1], parent)
            
        temp = []
        for t in range(1, n+1):
            temp.append(find(t, parent))
            
        # print(temp)
        counter = Counter(temp)
        counter = list(counter.values())
        minimum = min(minimum, abs(counter[0] - counter[1]) if len(counter) != 1 else counter[0]) 
    return minimum



# from collections import Counter

# def solution(n, wires):
#     answer = int(1e9)


#     for i in range(n-1) : 
#         parent = [x for x in range(n + 1)]
#         new_wires = []
#         for j in range(n-1) :
#             if i == j :
#                 continue
#             new_wires.append(wires[j])

#         for wire in new_wires :
#             a, b = wire
#             union_parent(parent, a, b)

#         new = []
#         for i in range(1, n + 1) :
#             new.append(find_parent(parent, i))

#         counter = Counter(new)
#         counter = list(counter.values())

#         answer = min(answer, abs(counter[0] - counter[1]))


#     return answer


            