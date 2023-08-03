def rev (s):
    return s[::-1]

def tail (s):
    return s[1:]

def check(s):
    from math import ceil
    sp_len = ceil(len(s) / 3)
    sp = s[:sp_len]
    if s == sp + rev(sp) + sp or \
        s == sp + tail(rev(sp)) + sp or \
            s == sp + rev(sp) + tail(sp) or \
                s == sp + tail(rev(sp)) + tail(sp):
        return 1
    return 0

for i in range(int(input())):
    print(check(input()))
        