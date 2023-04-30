n = int(input())
lst = list(map(int, input().split()))
mount = int(input())
lst.sort()
def param(lst, m):
    temp = [i if i <= m else m for i in lst]
    return sum(temp) <= mount

def bi_search(lst, start, end):
    while start <= end:
        mid = (start + end) // 2
        if param(lst, mid):    # 예산보다 적은지?
            start = mid + 1
        else:
            end = mid - 1
    return end

print(bi_search(lst, 1, lst[-1]))
