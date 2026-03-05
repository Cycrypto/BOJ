import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if m < n or m > 26 * n:
    sys.stdout.write("!")
else:
    s = ['A'] * n
    cost = m - n

    i = n - 1
    while cost and i >= 0:
        add = 25 if cost >= 25 else cost
        s[i] = chr(ord('A') + add)
        cost -= add
        i -= 1

    sys.stdout.write(''.join(s))