import heapq
import sys

input = sys.stdin.readline

n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort()

pq = []

for dl, cup in jobs:
    heapq.heappush(pq, cup)
    if len(pq) > dl:
        heapq.heappop(pq)

print(sum(pq))