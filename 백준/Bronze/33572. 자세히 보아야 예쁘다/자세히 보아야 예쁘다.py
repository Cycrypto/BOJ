n, m = map(int, input().split())
A = sum(list(map(int, input().split()))) - n
print("DIMI" if A >= m else "OUT")
