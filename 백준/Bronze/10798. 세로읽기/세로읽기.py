lst = [input() for _ in range(5)]
max_len = len(max(lst, key=len))
result = ''
for idx, l in enumerate(lst):
    if len(l) < max_len:
        l += ' ' * (max_len - len(l))
        lst[idx] = l

for s in zip(*lst):
    result += ''.join(s)
print(result.replace(' ',''))