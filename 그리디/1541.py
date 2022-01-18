inp = input().split('-')

for i in range(len(inp)):
    if '+' in inp[i]:
        inp[i] = sum(map(int, inp[i].split('+')))
inp = list(map(int, inp))
result = inp[0]
for j in range(1, len(inp)):
    result -= inp[j]

print(result)