import sys
from math import prod

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    s = {}
    for _ in range(int(input())):
        a, b = input().split()
        s[b] = s.get(b, 0) + 1

    print(prod(v + 1 for v in s.values()) - 1)