from itertools import combinations_with_replacement as combinations
a,b = map(int, input().split())
for i in combinations([i for i in range(1,a+1)], b):
    print(*i)
