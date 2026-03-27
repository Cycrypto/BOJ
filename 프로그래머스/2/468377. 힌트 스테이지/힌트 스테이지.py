def solution(cost, hint):
    final_stage = len(cost)
    hint_storage = [0] * (final_stage + 1)
    
    def dfs(stage, storage, score):
        if stage == final_stage:
            return score
        
        hint_count = min(storage[stage], len(cost[stage]) - 1)

        storage = storage.copy()
        storage[stage] = 0

        score += cost[stage][hint_count]

        # 마지막 스테이지는 hint가 없음
        if stage == final_stage - 1:
            return score
        
        cp_storage = storage.copy()
        cp_score = score + hint[stage][0]
        for h in hint[stage][1:]:
            cp_storage[h - 1] += 1
        
        next_stage = stage + 1
        return min(
            dfs(next_stage, storage, score),
            dfs(next_stage, cp_storage, cp_score)
        )
    
    return dfs(0, hint_storage, 0)