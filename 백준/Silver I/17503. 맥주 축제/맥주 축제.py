import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())

# 선호도 순서로 정렬하여 입력
beers = [list(map(int, input().split())) for _ in range(k)]
beers = sorted(beers,key=lambda x: (x[1],x[0]))
preference = 0
pq = []

for i in beers:
    preference += i[0]
    heapq.heappush(pq, i[0])

    if len(pq) == n:
        if preference >= m:
            answer = i[1]
            break
        else:
            preference -= heapq.heappop(pq)
else:
    print(-1)
    exit()

print(answer)