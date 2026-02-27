import heapq
import sys
input = sys.stdin.readline
hq = []

for _ in range(int(input())):
    op = int(input())
    if op == 0:
        print(heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, op)

