N = int(input())
graph = [list(input()) for _ in range(N)]
result = ""
def check(x, y, s):
    lst = [graph[i][y:y+s] for i in range(x, x+s)]
    if len(set(k:=sum(lst, []))) == 1:
        return True, k[0]
    else:
        return False, k[0]

def qurd(x, y, s):
    global result
    if (r:=check(x,y,s))[0] or s == 1:
        result += str(r[1])
        return
    div = s // 2
    result += "("
    qurd(x,y,div)
    qurd(x,y+div,div)
    qurd(x+div,y,div)
    qurd(x+div,y+div,div)
    result +=")"

qurd(0, 0, N)
print(result)