from itertools import combinations


def solution(n, q, ans):
    cnt = 0
    for comb in combinations(range(1, n+1), 5):
        is_ok = True
        for x, i in enumerate(q):
            if len(set(comb) & set(i)) != ans[x]:
                is_ok = False
        if is_ok:
            cnt += 1
    return cnt