i = int(input())
MEM = [0 for _ in range(i + 1)]
MEM[0] = 1
MEM[1] = 2

def solve(tesk):
    if tesk <= 1:
        return MEM[tesk]

    if MEM[tesk] != 0:
        return MEM[tesk]

    else:
        MEM[tesk] = solve(tesk - 1) + solve(tesk - 2)
        return MEM[tesk]
solve(i)
print(MEM[i] * 2)