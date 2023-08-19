n, a, d = map(int, input().split())
note = list(map(int, input().split()))
l = max(note)
#s = [i for i in range(a, l+1, d)]

j = 0
res = 0
s = a
for i in note:
    if j == l+1:
        break
    
    if i == s:
        res += 1
        s += d

print(res)