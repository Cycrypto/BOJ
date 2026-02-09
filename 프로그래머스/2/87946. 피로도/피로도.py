def dfs(fatigue, dungeons):
    best = 0
    for i, (req, cost) in enumerate(dungeons):
        if fatigue >= req:
            best = max(best, 1 + dfs(fatigue - cost, dungeons[:i] + dungeons[i+1:]))
    return best

def solution(k, dungeons):
    return dfs(k, dungeons)
