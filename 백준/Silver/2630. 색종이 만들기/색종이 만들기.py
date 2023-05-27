import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt =[0, 0]

def conq(x, y, n):
    lst = [graph[i][y:y+n] for i in range(x, x+n)]
    if len(set(k:=sum(lst, []))) == 1:
        cnt[k[0]] += 1
        return
    
    d = n // 2
    for i in range(0, n, d):
        for j in range(0, n, d):
            conq(x+i, y+j, d)

conq(0, 0, N)
print(cnt[0])
print(cnt[1])