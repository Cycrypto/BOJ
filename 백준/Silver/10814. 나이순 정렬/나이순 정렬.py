import sys

input = sys.stdin.readline


n = int(input())
d = []
for i in range(n):
    k, v = input().split()
    d.append([i, int(k), v])

d.sort(key= lambda x: (x[1], x[0]))

for a, b, c in d:
    print(b, c)