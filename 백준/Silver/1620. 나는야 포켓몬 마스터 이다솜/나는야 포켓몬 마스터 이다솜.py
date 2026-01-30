import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s1 = {}
s2 = {}

for i in range(1, n + 1):
    s1[name := input().strip()] = i
    s2[i] = name

for _ in range(m):
    a = input().strip()
    if a.isdigit():
        num = int(a)
        print(s2[num])
    else:
        print(s1[a])