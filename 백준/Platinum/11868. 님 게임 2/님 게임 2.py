n = int(input())
stone = list(map(int, input().split()))
result = 0
for p in stone:
    result ^=p

print("koosaga" if result != 0 else "cubelover")