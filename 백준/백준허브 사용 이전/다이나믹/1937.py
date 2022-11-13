up = lambda x, y: (x, y-1)
down = lambda x, y: (x, y+1)
left = lambda x, y: (x-1, y)
right = lambda x, y: (x+1, y)


n = int(input())
mem = [[-1] * n] * n
_map = [[int(i) for i in input().split()] for i in range(n)]


def dfs(x, y):
    if x >= n or y >= n or x < 0 or y < 0:
        return
    # 기저사례 : 판을 벗어난 경우

    for k in [up, down, left, right]:
        mx, my = k(x, y)
        print(_map[mx][my])



print(dfs(0, 0))

# for i in range(_map):
#     min_len = 0
#     for j in range(i):
#         for k in [up, down, left, right]:
#             if k >= n or k < 0:
#                 continue    # 맵을 벗어난 경우
#             else:
#                 min_len = min(min_len, _map[])