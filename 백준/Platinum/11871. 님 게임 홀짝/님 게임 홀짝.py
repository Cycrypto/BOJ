n = int(input())
stone = list(map(int, input().split()))
result = 0
for p in stone:
    result ^= (p + 1) // 2 if p % 2 != 0 else (p-1)//2

print("koosaga" if result != 0 else "cubelover")