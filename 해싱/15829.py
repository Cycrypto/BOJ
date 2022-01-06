r = 31
M = 1234567891


def hash(s):
    result = 0
    for index, i in enumerate(s):
        result += (ord(i) - 96) * (r ** index)
    return result % M

input()
print(hash(input()))
