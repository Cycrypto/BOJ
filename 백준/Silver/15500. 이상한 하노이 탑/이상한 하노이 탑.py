n = int(input())
m = int(n)

s1, s2 = [list(map(int, input().split())), 1], [[],2]
c = []

def solve(select, to):
    global m
    empty = lambda x: len(x) == 0

    if empty(select[0]) and empty(to[0]):
        return
    
    while not empty(select[0]):
        p = select[0].pop()

        if p == m:  # 찾는 수가 나오면 3으로 이동
            m -= 1
            c.append([select[1], 3])
            
        else:
            to[0].append(p)
            c.append([select[1], to[1]])
    
    solve(to, select)

solve(s1, s2)

print(len(c))
for i in c:
    print(*i)