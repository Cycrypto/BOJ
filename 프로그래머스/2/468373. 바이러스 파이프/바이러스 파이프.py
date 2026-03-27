from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n)]
    for x, y, pipe_type in edges:
        x -= 1
        y -= 1
        graph[x].append((y, pipe_type))
        graph[y].append((x, pipe_type))

    init_state = [0] * n
    init_state[infection - 1] = 1

    def bfs(pipe, state):
        q = deque(i for i, v in enumerate(state) if v)

        while q:
            cur = q.popleft()

            for nxt, color in graph[cur]:
                if color != pipe:
                    continue
                if state[nxt]:
                    continue

                state[nxt] = 1
                q.append(nxt)

        return state

    def dfs(prev_pipe, infection_state, depth):
        res = infection_state

        if depth == k:
            return infection_state

        for pipe in range(1, 4):
            if pipe != prev_pipe:
                next_state = bfs(pipe, infection_state[:])
                nxt = dfs(pipe, next_state, depth + 1)

                if sum(res) < sum(nxt):
                    res = nxt

        return res

    best = dfs(0, init_state, 0)
    return sum(best)