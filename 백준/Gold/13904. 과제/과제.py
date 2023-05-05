import heapq
lst = []
for i in range(n:=int(input())):
    n, m = map(int, input().split())
    lst.append([-m, n])

result = [0 for _ in range(1001)]
heapq.heapify(lst)
while lst:
    p = heapq.heappop(lst)
    for i in range(p[1], 0, -1):
        if result[i] == 0:
            result[i] = -p[0]
            break
    
print(sum(result))