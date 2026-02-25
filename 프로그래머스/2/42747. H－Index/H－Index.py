def solution(citations):
    citations.sort()
    n = len(citations)
    left, right = 0, len(citations)
    
    while left < right:
        mid = (left + right) // 2
        h = n - mid
        if citations[mid] < h:
            left = mid + 1
        else:
            right = mid
    return n - left