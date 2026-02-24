import sys
from collections import deque

def main():
    input = sys.stdin.readline

    # 첫 줄은 일단 읽되, 로컬에서 N/M을 헷갈려도 안 터지게
    # 실제로 들어온 지도(lines) 기준으로 크기를 확정한다.
    a, b = map(int, input().split())

    lines = [line.rstrip('\n') for line in sys.stdin.read().splitlines() if line.strip() != '']
    if not lines:
        return

    H0 = len(lines)
    W0 = len(lines[0])

    # BOJ 스펙대로면: (가로=a, 세로=b) => H=b, W=a
    # 로컬에서 반대로 쓰면: H=a, W=b 가 될 수 있음
    if H0 == b and all(len(row) == a for row in lines):
        W, H = a, b
    elif H0 == a and all(len(row) == b for row in lines):
        W, H = b, a
    else:
        # 첫 줄 숫자가 실제 지도와 안 맞는 로컬 입력을 위해, 실제 지도 크기를 사용
        W, H = W0, H0

    grid = [list(row) for row in lines[:H]]

    # 아이템(X) 좌표 -> 비트 인덱스
    item_id = [[-1] * W for _ in range(H)]
    sr = sc = er = ec = -1
    idx = 0

    for r in range(H):
        for c in range(W):
            ch = grid[r][c]
            if ch == 'S':
                sr, sc = r, c
            elif ch == 'E':
                er, ec = r, c
            elif ch == 'X':
                item_id[r][c] = idx
                idx += 1

    full = (1 << idx) - 1

    # dist[r][c][mask] = (r,c)에 mask 상태로 도달한 최소 시간
    dist = [[[-1] * (1 << idx) for _ in range(W)] for __ in range(H)]
    q = deque([(sr, sc, 0)])
    dist[sr][sc][0] = 0

    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)

    while q:
        r, c, mask = q.popleft()
        d = dist[r][c][mask]

        if r == er and c == ec and mask == full:
            print(d)
            return

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if grid[nr][nc] == '#':
                continue

            nmask = mask
            iid = item_id[nr][nc]
            if iid != -1:
                nmask |= (1 << iid)

            if dist[nr][nc][nmask] == -1:
                dist[nr][nc][nmask] = d + 1
                q.append((nr, nc, nmask))

    print(-1)

if __name__ == "__main__":
    main()