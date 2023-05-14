N, K, A, B = map(int, input().split())
plant = sorted([K for _ in range(N)])

cnt = 0
while 0 not in plant:
    plant = sorted(list(map(lambda x:x-1, plant)))  # 1 감소
    plant[:A] = list(map(lambda x:x+B, plant[:A]))
    cnt += 1
print(cnt)