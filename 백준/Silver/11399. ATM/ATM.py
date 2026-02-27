n = int(input())
s = sorted(list(map(int, input().split())))
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = s[i - 1] + p[i - 1]
print(sum(p))