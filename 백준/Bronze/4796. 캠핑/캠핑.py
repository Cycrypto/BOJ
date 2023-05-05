i = 1
while True:
    l, p, v = map(int, input().split())
    if sum([l, p, v]) == 0:
        break
    d = v%p if v%p <= l else l
    print(f"Case {i}: {d + v//p * l}")
    i+=1