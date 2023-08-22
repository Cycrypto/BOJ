pattern = input()

def get_max(p, rev):
    tmp = 0
    res = ""

    for s in p:
        if s == 'K':
            if tmp and not rev:
                res += str(10**tmp+5)
                tmp = 0
            
            elif tmp and rev:
                res += str(5 * (10**tmp))
                tmp = 0

            else:
                res += "5"
            
        
        else:
            tmp += 1
        

    if tmp:
        if not rev:
            res += str(10 ** (tmp - 1))
        else:
            while tmp:
                res += "1"
                tmp -= 1

    return res

print(get_max(pattern, True))
print(get_max(pattern, False))
