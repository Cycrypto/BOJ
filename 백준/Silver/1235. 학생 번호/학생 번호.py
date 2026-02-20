k = int(input())
students = [list(input().strip())for _ in range(k)]

m = len(students[0])

for i in range(1, m+1):
    seen = set()
    for s in students:
        seen.add(''.join(s[-i:]))

    if len(seen) == k:
        print(i)
        break
