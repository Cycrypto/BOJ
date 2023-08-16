import sys
sys.setrecursionlimit(int(1e8))
MAX = 1001
INF = 1e9+7
dp = [[-1]* MAX for _ in range(MAX)]
trace = []
def get_dist(a, b):
    # print(a, b)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(posA, posB):

    if posA == m or posB == m:
        return 0
    
    if dp[posA][posB] != -1:
        return dp[posA][posB]
    
    nxt = max(posA, posB)+1
    # print(posA, posB, nxt)
    if not posA:
        dp[posA][posB] = solve(nxt, posB) + get_dist([1,1], events[nxt])
    else:
        dp[posA][posB] = solve(nxt, posB) + get_dist(events[posA], events[nxt])
    
    if not posB:
        dp[posA][posB] = min(solve(posA, nxt) + get_dist([n, n], events[nxt]), dp[posA][posB])
    else:
        dp[posA][posB] = min(solve(posA, nxt) + get_dist(events[posB], events[nxt]), dp[posA][posB])

    return dp[posA][posB]

def reconstruct(posA, posB):
    if posA == m or posB == m:
        return
    
    nxt = max(posA, posB)+1   
    
    if not posA:
        a = solve(nxt, posB) + get_dist([1, 1], events[nxt])
    else:
        a = solve(nxt, posB) + get_dist(events[posA], events[nxt])
    
    if not posB:
        b = solve(posA, nxt) + get_dist([n, n], events[nxt])
    else:
        b = solve(posA, nxt) + get_dist(events[posB], events[nxt])
    
    if a > b:
        trace.append(2)
        reconstruct(posA, nxt)
    else:
        trace.append(1)
        reconstruct(nxt, posB)


n = int(input())
m = int(input())
events = [[]]*(m+1)
for i in range(1, m+1):
    events[i] = list(map(int, input().split()))

print(solve(0, 0))
reconstruct(0, 0)
for i in trace:
    print(i)