import heapq
heap = []
max_heap = []

for i in range(int(input())):
    for j in range(int(input())):
        op, k = input().split()
        if op == 'I':
            heapq.heappush(heap, k)
            heapq.heappush(max_heap * -1, k)

        elif op == 'D':
            if len(heap) == 0:
                pass

            elif k == '1':
                max_value = heapq.heappop(heap)
                heap.remove(max_value)

            else:
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value * -1, min_value))

    if heap:
        print(heapq.heappop(max_heap)[1], heapq.heappop(heap))
    else:
        print("EMPTY")