from itertools import permutations
n, m = map(int, input().split())
n = [i for i in range(1, n+1)]
for j in permutations(n, m):
    print(*j)