n, k = map(int, input().split())
result = 0;
while bin(n).count('1') > k:
    n += 1
    result += 1

print(result)