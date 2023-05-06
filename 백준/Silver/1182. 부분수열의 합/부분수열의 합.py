n, s = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
ss = 0

def dfs(current):
    global ss, result
    if current == n:
        return  # 탈출 조건
    
    if ss + lst[current] == s:
        result += 1
    
    dfs(current+1)
    
    ss += lst[current]
    dfs(current+1)

    ss -= lst[current]

dfs(0)
print(result)
