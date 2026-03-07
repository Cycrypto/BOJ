import sys

input = sys.stdin.readline

N = int(input())
W = int(input())

cases = [(0, 0)]
for _ in range(W):
    x, y = map(int, input().split())
    cases.append((x, y))


def dist1(a, nxt):
    if a == 0:
        x1, y1 = 1, 1
    else:
        x1, y1 = cases[a]
    x2, y2 = cases[nxt]
    return abs(x1 - x2) + abs(y1 - y2)


def dist2(b, nxt):
    if b == 0:
        x1, y1 = N, N
    else:
        x1, y1 = cases[b]
    x2, y2 = cases[nxt]
    return abs(x1 - x2) + abs(y1 - y2)


sys.setrecursionlimit(10 ** 6)
dp = [[-1] * (W + 1) for _ in range(W + 1)]


def solve(a, b):
    nxt = max(a, b) + 1
    if nxt > W:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    move1 = solve(nxt, b) + dist1(a, nxt)
    move2 = solve(a, nxt) + dist2(b, nxt)

    dp[a][b] = min(move1, move2)
    return dp[a][b]


def trace(a, b):
    nxt = max(a, b) + 1
    if nxt > W:
        return

    move1 = solve(nxt, b) + dist1(a, nxt)
    move2 = solve(a, nxt) + dist2(b, nxt)

    if move1 <= move2:
        print(1)
        trace(nxt, b)
    else:
        print(2)
        trace(a, nxt)
print(solve(0, 0))
trace(0, 0)