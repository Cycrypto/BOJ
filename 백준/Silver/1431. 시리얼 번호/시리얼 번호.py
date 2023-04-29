serial = []
for i in range(int(input())):
    serial.append((n := input(), len(n)))

serial.sort(key= lambda x: x[1])

for i in range(len(serial)):
    for j in range(i, len(serial)):
        if serial[i][1] == serial[j][1]:
            find = lambda x: sum([int(i) for i in x if i in "123456789"])
            a = find(serial[i][0])
            b = find(serial[j][0])
            if a > b:
                serial[i], serial[j] = serial[j], serial[i]
            if a == b:
                serial[i], serial[j] = sorted([serial[i], serial[j]])
                
for result in serial:
    print(result[0])