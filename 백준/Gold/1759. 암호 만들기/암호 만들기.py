from itertools import combinations

# 입력 받기
L, C = map(int, input().split())
alphabets = sorted(input().split())

# 조합 생성하기
comb = combinations(alphabets, L)

# 조건 검사하기
for c in comb:
    vowel_count = 0
    consonant_count = 0
    for ch in c:
        if ch in 'aeiou': # 모음인 경우
            vowel_count += 1
        else: # 자음인 경우
            consonant_count += 1
    if vowel_count >= 1 and consonant_count >= 2: # 조건을 만족하는 경우
        print(''.join(c)) # 암호 출력하기