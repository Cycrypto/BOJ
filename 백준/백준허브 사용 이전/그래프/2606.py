from sys import stdin
read = stdin.readline

def bfs (start, dic):
    queue = [start]
    while queue:    # 큐가 차있는 동안~
        for i in dic[queue.pop()]:
            if i not in visited:    # 현재 노드가 방문되지 않았다면
                visited.append(i)    # visited에 현재 노드를 추가
                queue.append(i)     # 큐에 현재 노드를 추가

dic = {}
for i in range(int(read())):
    dic[i+1] = set()

for i in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)   # 트리 구성

visited = []
bfs(1, dic)
print(len(visited) - 1)