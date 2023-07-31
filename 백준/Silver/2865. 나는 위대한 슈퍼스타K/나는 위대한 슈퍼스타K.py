n,m,k = map(int, input().split())
info = {i:[] for i in range(1, n+1)}
for i in range(m):
    genre = input().split()
    for j in range(0, (n*2), 2):
        kk, v = genre[j:j+2]
        info[int(kk)].append(float(v))

s = []
for v in info.values():
    s.append(max(v))
s.sort(reverse=True)
print(round(sum(s[:k]), 1))