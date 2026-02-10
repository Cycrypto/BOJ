def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    overlap = lost & reserve
    lost -= overlap
    reserve -= overlap

    for x in sorted(lost):
        if x - 1 in reserve:
            reserve.remove(x - 1)
        elif x + 1 in reserve:
            reserve.remove(x + 1)
        else:
            n -= 1

    return n
