n = int(input())
extractor = {}

for _ in range(n):
    name, ext = input().split('.')
    if ext in extractor.keys():
        extractor[ext] += 1
    else:
        extractor[ext] = 1

for k in sorted(list(extractor.keys())):
    print(k, extractor[k])
