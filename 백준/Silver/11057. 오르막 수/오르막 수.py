N = int(input())
mem = [[0]*9 for _ in range(N+2)]
mem[1] = [1] * 10

for i in range(2, N+2):
    tmp = [0]*10
    tmp[0] = sum(mem[i-1])
    for j in range(1, 10):
        tmp[j] = tmp[j-1] - mem[i-1][j-1]
    mem[i] = tmp

print(mem[N+1][0] % 10007)