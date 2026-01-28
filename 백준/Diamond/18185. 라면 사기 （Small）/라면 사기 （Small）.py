import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a += [0, 0]

cost = 0

for i in range(n):
    if a[i+1] > a[i+2]:
        x = min(a[i], a[i+1] - a[i+2])
        cost += 5 * x
        a[i] -= x
        a[i+1] -= x

        y = min(a[i], a[i+1], a[i+2])
        cost += 7 * y
        a[i] -= y
        a[i+1] -= y
        a[i+2] -= y
    else:
        y = min(a[i], a[i+1], a[i+2])
        cost += 7 * y
        a[i] -= y
        a[i+1] -= y
        a[i+2] -= y

        x = min(a[i], a[i+1])
        cost += 5 * x
        a[i] -= x
        a[i+1] -= x

    cost += 3 * a[i]
    a[i] = 0

print(cost)
