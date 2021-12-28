from itertools import combinations


def solve(arr):
    result = 0
    for i in list(combinations(arr, 2)):
        result += (i[0] * i[1])
    return result % 1000000007


input()
print(solve(list(map(int, input().split(' ')))))