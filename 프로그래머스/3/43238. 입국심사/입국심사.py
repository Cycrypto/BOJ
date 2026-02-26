import math

def solution(n, times):
    left, right = 0, max(times) * n
    
    while left <= right:
        p = 0    
        mid = (left + right) // 2
        for t in times:
            p += math.ceil(mid // t)
            
        if p >= n:
            right = mid - 1
            
        else:
            left = mid + 1
    return left