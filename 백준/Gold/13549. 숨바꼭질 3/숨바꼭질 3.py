import heapq
INF = int(1e9)

N, K = map(int, input().split())  # 시작 위치, 도착 위치
distance = [INF]*100001  # 100001개의 떨어진 거리

def dijkstra(start):  # 다익스트라
    distance[start] = 0  # 시작 위치 초기화
    q = []
    heapq.heappush(q, (0, start))  # 시작 위치 우선 순위 큐 삽입

    while q:  # q에 값이 있을 동안
        dist, now = heapq.heappop(q)  # 거리가 가장 짧은 노드
        if distance[now] < dist:
            continue
        for a, b in [(now*2, dist), (now+1, dist+1), (now-1, dist+1)]:  # 2배, 오른쪽, 왼쪽
            if 0 <= a <= 100000 and distance[a] > b:  # 범위 안에 있고 방문하지 않았다면(범위 주의)
                distance[a] = b
                heapq.heappush(q, (b, a))

dijkstra(N)  # 시작 위치 다익스트라 실행
print(distance[K])  # 시작 위치로부터 K