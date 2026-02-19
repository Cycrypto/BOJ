n, m = map(int, input().split())
deck = list(map(int, input().split()))
result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = sum([deck[i], deck[j], deck[k]])
            result = max(result, s) if s <= m else result
print(result)