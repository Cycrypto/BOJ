'''
A -> B -> BA -> BAB -> BABBA
A -> B
B - > BA
B, BA, BAB, BABBA, BABBABAB, BABBABABBABBA
0 1
1 1
1 2
2 3
3 5
.
.
.

'''
i = int(input())
MEM = [0 for _ in range (i+1)]
MEM[1] = 1
def fivo(k):
    if k <= 1:
        return k
    if MEM[k] != 0:
        return MEM[k]

    else:
        MEM[k] = fivo(k-1) + fivo(k-2)
        return MEM[k]


fivo(i)
print(MEM[-2], MEM[-1])