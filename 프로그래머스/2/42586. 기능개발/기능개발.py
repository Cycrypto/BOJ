def solution(progresses, speeds):
    days = [(100 - p + speeds[i] - 1) // speeds[i] for i, p in enumerate(progresses)]
    l, r = 0, 0
    result = 0
    res =  []
    while r < len(days) - 1:
        if days[r + 1] > max(days[l:r+1]):
            res.append(r - l + 1)
            l = r + 1
        r += 1
    res.append(r - l + 1)
    return res