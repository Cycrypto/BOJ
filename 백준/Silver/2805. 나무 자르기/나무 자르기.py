def func(lst, m):
    res = []
    for i in lst:
        if i - m > 0:
            res.append(i-m)
        else:
            res.append(0)
    return sum(res) >= goal

def bi_search(lst, start, end):

    while start + 1 != end:
        mid = (start + end) // 2
        if func(lst, mid):
            start = mid
        
        else:
            end = mid

    return start, end

result = 0
n, goal = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

print(bi_search(lst, 0, lst[-1])[0])