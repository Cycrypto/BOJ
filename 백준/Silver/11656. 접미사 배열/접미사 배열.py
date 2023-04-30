st = input()
suffix = []

for i in range(len(st)):
    suffix.append(st[i:])

suffix.sort()
for s in suffix:
    print(s)