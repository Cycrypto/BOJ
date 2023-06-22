def is_match_cached(pattern, suffix, cache=None):
    if cache is None:
        cache = {}

    if (pattern, suffix) in cache:
        return cache[(pattern, suffix)]

    pos = 0

    while pos < len(suffix) and pos < len(pattern) and \
        (pattern[pos] == '?' or pattern[pos] == suffix[pos]): 
        pos += 1

    if pos == len(pattern):
        result = pos == len(suffix)
    elif pattern[pos] == '*':
        result = False
        for i in range(len(suffix)):
            if pos+i > len(suffix):
                break
            if is_match_cached(pattern[pos+1:], suffix[pos+i:], cache):
                result = True
                break
    else:
        result = False

    cache[(pattern, suffix)] = result
    return result 

pattern = input()
for i in range(int(input())):
    if pattern == '*':
        print(input())

    elif(is_match_cached(pattern, k:=input())):
        print(k)
    else:
        continue