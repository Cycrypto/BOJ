from bisect import bisect_left
result = [0, 0]
def solution(s):
    while s != '1':
        index = bisect_left(sorted(list(s)), '1')   # 0의 갯수
        result[1] += index
        result[0] += 1
        s = str(bin(len(s) - index)[2:])
        
    return result
    