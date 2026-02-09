from math import sqrt
from itertools import permutations

def is_prime(num: int):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(map(int, numbers))
    cnt = 0
    d = []
    for i in range(1, len(numbers) + 1):
        d += [''.join(map(str, j)) for j in permutations(numbers, i)]
    
    for j in list(set(map(int, d))):
            if int(j) >= 2 and is_prime(int(j)):
                cnt += 1
    return cnt