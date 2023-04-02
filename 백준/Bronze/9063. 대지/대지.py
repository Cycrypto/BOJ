spot = int(input())
x = [0 for _ in range(spot)]
y = [0 for _ in range(spot)]

for i in range(spot):
    x[i], y[i] = map(int, input().split())

if spot <= 1:
    print(0)
    exit()

print((max(x) - min(x)) * (max(y) - min(y)))