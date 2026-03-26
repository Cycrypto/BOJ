def solution(cost, hint):
    n = len(cost)
    
    def add_bundle(cnt, bundle):
        nxt = cnt[:]
        for stage_no in bundle[1:]:
            nxt[stage_no - 1] += 1
        return nxt
    
    def dfs(i, cnt):
        clear = cost[i][min(cnt[i], n-1)]
        
        if i == n - 1:
            return clear
        
        next_cnt = cnt[:]
        next_cnt[i] = 0
        
        skip = clear + dfs(i + 1, next_cnt)
        buy = clear + hint[i][0] + dfs(i + 1, add_bundle(cnt, hint[i]))
        
        return min(skip, buy)
    return dfs(0, [0] * n)