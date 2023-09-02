MAX_PARTY = 200
start, end = [0]*MAX_PARTY, [0]*MAX_PARTY

def print_result(d,c):
    print(f"On day {d} Emma can attend as many as {c} parties.")


def best_index(t, np):
    index = -1
    earliest = 33

    for i in range(np):
        if start[i] <= t < end[i] and end[i] < earliest:
            index = i
            earliest = end[i]
    return index


p = int(input())
day = 0
while p:
    day += 1
    for i in range(p):
        s, e = map(int, input().split())
        start[i] = (s-8)*2
        end[i] = (e-8)*2
    
    count = 0
    for i in range(32):
        index = best_index(i, p)
        if index >= 0:
            count += 1
            start[index] = 32

    print_result(day, count)
    p = int(input())
