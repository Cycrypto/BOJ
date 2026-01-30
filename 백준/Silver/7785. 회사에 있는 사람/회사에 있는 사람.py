import sys
input = sys.stdin.readline

n = int(input().strip())
current = set()
for _ in range(n):
    name, action = input().split()
    if action == "enter":
        current.add(name)
    else:
        current.remove(name)
for name in sorted(current, reverse=True):
    print(name)
