mmax = 0
c, r = 0, 0
for i in range(9):
    line = list(map(int, input().split()))
    for idx, j in enumerate(line):
        if j > mmax:
            mmax = j
            c = i
            r = idx

print(mmax)
print(c + 1, r + 1)