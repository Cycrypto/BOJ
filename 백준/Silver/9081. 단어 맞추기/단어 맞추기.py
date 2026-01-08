import sys

input = sys.stdin.readline


for rep in range(int(input())):
    a = list(input().strip())
    result = ''.join(a)
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i+1]:
            for j in range(len(a) - 1, -1, -1):
                if a[j] > a[i]:
                    a[i], a[j] = a[j], a[i]
                    break
            result = ''.join(a[:i+1] + list(reversed(a[i+1:])))
            break
    print(result)
