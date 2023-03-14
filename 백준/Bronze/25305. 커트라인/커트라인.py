p = lambda:map(int, input().split())
_, cut = p()
print(sorted(list(p()), reverse=True)[cut - 1])
