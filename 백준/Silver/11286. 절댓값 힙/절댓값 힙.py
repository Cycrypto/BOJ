import sys
import heapq
input = sys.stdin.readline


n = int(input())
hq = []

for _ in range(n):
    op = int(input())
    if op != 0:
        heapq.heappush(hq, (abs(op), op))
    else:
        print(heapq.heappop(hq)[1] if hq else 0)