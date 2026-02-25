import math
def solution(progresses, speeds):
    daily = [math.ceil((100 - p)/speeds[i]) for i, p in enumerate(progresses)]
    result = []
    curr = daily[0]
    cnt = 0
    
    for right in daily:
        if right > curr:
            curr = right
            result.append(cnt)
            cnt = 1
        else:
            cnt += 1
    result.append(cnt)
    return result