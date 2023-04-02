inp = []
for i in range(4):
    inp.append(int(input()))

s_time = sum(inp)
print(s_time // 60)
print(s_time % 60)