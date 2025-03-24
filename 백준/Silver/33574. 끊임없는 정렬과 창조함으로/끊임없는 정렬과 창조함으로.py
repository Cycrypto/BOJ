s = []
for i in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s.sort() if query[1] == 1 else s.sort(reverse=True)
    else:
        if query[1] == 0:
            s.insert(0, query[2])
        elif query[1] == len(s):
            s.append(query[2])
        else:
            s.insert(query[1], query[2])

print(len(s))
print(*s)