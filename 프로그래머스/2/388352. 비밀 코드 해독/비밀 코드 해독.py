from itertools import combinations

def solution(n, q, ans):
    res = 0
    
    for comb in combinations(range(1, n + 1), 5):
        valid = True
        
        for d, query in enumerate(q):
            c = 0
            for j in range(5):
                if comb[j] in query:
                    c += 1
            
            if c != ans[d]:
                valid = False
                break
        
        if valid:
            res += 1
    
    return res