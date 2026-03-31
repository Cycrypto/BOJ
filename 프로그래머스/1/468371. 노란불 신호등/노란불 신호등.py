from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)


def solution(signals):
    info = []
    total_cycle = 1
    
    for g, y, r in signals:
        cycle = g + y + r
        info.append((g, y, cycle))
        total_cycle = lcm(total_cycle, cycle)
    
    for t in range(1, total_cycle + 1):
        ok = True
        for g, y, cycle in info:
            phase = (t - 1) % cycle + 1
            if not (g < phase <= g + y):
                ok = False
                break
        if ok:
            return t
    return -1