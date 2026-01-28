import sys
input = sys.stdin.readline

n, b, c = map(int, input().split())
a = list(map(int, input().split()))
a += [0, 0]

if c >= b:
    print(sum(a[:n]) * b)
    sys.exit(0)

cost1 = b
cost2 = b + c
cost3 = b + 2 * c

ans = 0

for i in range(n):
    if a[i + 1] > a[i + 2]:
        x = min(a[i], a[i + 1] - a[i + 2])
        ans += cost2 * x
        a[i] -= x
        a[i + 1] -= x

        y = min(a[i], a[i + 1], a[i + 2])
        ans += cost3 * y
        a[i] -= y
        a[i + 1] -= y
        a[i + 2] -= y
    else:
        y = min(a[i], a[i + 1], a[i + 2])
        ans += cost3 * y
        a[i] -= y
        a[i + 1] -= y
        a[i + 2] -= y

        x = min(a[i], a[i + 1])
        ans += cost2 * x
        a[i] -= x
        a[i + 1] -= x

    ans += cost1 * a[i]
    a[i] = 0

print(ans)
