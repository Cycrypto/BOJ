import heapq
INF = float('inf')
MAP = {
    'A' : {'B': 2, 'C' : 3},
    'B' : {'C' : 4, 'D' : 5},
    'C' : {'D' : 6},
    'D' : {},
    'E' : {'A' : 1}
}

MAP = {
    'A' : {'B': 8, 'C' : 1,'D':2},
    'B' : {},
    'C' : {'B' : 5, 'D' : 2},
    'D' : {'E':3,'F':5},
    'E' : {'F' : 1},
    'F' : {'A' : 5}
}

def dijkstra (road, start):
    country = {node:INF for node in road}   # [INF,INF,INF,INF,INF]
    cnt = 0
    country[start] = 0  #   [0, INF, INF, INF, INF]
    heap = []
    heapq.heappush(heap, [country[start], start])   #   [[0, 'A']]

    while heap:
        # print("heap",heap)
        current_distance, now_position = heapq.heappop(heap)    # 0, 'A'
        print(country[now_position], current_distance)
        if country[now_position] < current_distance:    # 현재 position이 이전 position보다 작으면
            continue                                    # 넘어간다

        # print("road_item :", road[now_position].items())

        for arrival, weight in road[now_position].items():
            distance = current_distance + weight
            if distance < country[arrival]: #도착지 거리가 현재 계산한 거리보다 작으면
                country[arrival] = distance #둘이 바꾼다
                heapq.heappush(heap, [distance, arrival])   #힙에 추가

        #     print("dist :",country[arrival])
        # print("\n\n\n")
    return country

print(dijkstra(MAP,'A'))
print(dijkstra(MAP,'B'))
print(dijkstra(MAP,'C'))
print(dijkstra(MAP,'D'))
print(dijkstra(MAP,'E'))
print(dijkstra(MAP,'F'))