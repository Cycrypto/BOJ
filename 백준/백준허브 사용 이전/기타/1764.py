a, b = map(int, input().split(' '))
listen = [input() for _ in range(a)]
see = [input() for _ in range(b)]
result = sorted(list(set(listen) & set(see)))
print(len(result))
for i in result:
    print(i)