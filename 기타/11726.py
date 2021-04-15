import itertools
def check(n):
    import math
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    result = 0
    card = [i for i in numbers]
    for e in range (1, len(card) + 1):
        for l in  list(set(list(map(''.join, itertools.permutations(card, e))))):

            if l[0] == '0':
                continue
            else:
                if check(int(l)) == True:
                    result = result + 1
    return result
print(solution("011"))