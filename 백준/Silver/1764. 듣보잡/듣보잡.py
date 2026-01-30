import sys
input = sys.stdin.readline
N, M = map(int, input().split())
heard = {input().strip() for _ in range(N)}
result = []

for _ in range(M):
    name = input().strip()
    if name in heard:
        result.append(name)
    result.sort()

print(len(result))
print("\n".join(result))