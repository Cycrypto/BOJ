i = int(input())
MEM = [0, 1]
for i in range(2, i+1):
    MEM.append(MEM[-1] + MEM[-2])
print(MEM[i])