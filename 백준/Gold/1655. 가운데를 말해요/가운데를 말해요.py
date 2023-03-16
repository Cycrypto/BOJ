import heapq
import sys
inputs = sys.stdin.readline
left_heap = []
right_heap = []

for i in range(int(inputs())):
    item = int(inputs())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -item)
    
    else:
        heapq.heappush(right_heap, item)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left_val = heapq.heappop(left_heap)
        right_val = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, -right_val)
        heapq.heappush(right_heap, -left_val)
    
    print(-left_heap[0])