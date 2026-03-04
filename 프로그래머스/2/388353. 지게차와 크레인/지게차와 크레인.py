from collections import deque

def solution(storage, requests):
    n, m = len(storage), len(storage[0])

    # 패딩: 밖(외부)을 '.'로 표현
    g = [['.'] * (m + 2)]
    for row in storage:
        g.append(['.'] + list(row) + ['.'])
    g.append(['.'] * (m + 2))

    H, W = n + 2, m + 2
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    for req in requests:
        ch = req[0]

        # 크레인: 해당 문자 전부 제거
        if len(req) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if g[i][j] == ch:
                        g[i][j] = '.'
            continue

        # 지게차: "요청 시점"에 외부와 연결된 면이 있는 ch만 제거 (연쇄 제거 X)
        visited = [[False] * W for _ in range(H)]
        q = deque([(0, 0)])
        visited[0][0] = True

        to_remove = []

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if visited[nx][ny]:
                    continue

                if g[nx][ny] == '.':          # 공기면 계속 확장
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif g[nx][ny] == ch:         # 공기와 맞닿은 타겟이면 제거 후보로만 기록
                    visited[nx][ny] = True
                    to_remove.append((nx, ny))
                else:
                    visited[nx][ny] = True    # 다른 컨테이너는 막힘(통과 불가)

        for x, y in to_remove:
            g[x][y] = '.'

    # 남은 컨테이너 개수
    return sum(g[i][j] != '.' for i in range(1, n + 1) for j in range(1, m + 1))