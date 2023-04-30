n, c = map(int, input().split())
stack = []
lst = list(map(int, input().split()))

for i in lst:
    flag = False
    for j in stack:
        if j[0] == i:
            j[1] += 1
            flag = True
    
    if not flag:
        stack.append([i, 1])
stack.sort(key= lambda x: x[1], reverse= True)
for i in stack:
    for j in range(i[1]):
        print(i[0], end=' ')