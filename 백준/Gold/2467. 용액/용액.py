n = int(input())
lst = list(map(int, input().split()))
start, end = 0, n-1    # 인덱스 번호를 가르킴
r1, r2 = start, end
mmin = 1e10

def find_min(x, y):
    global r1, r2, mmin
    if abs(lst[x] + lst[y]) < mmin:
        mmin = abs(lst[x] + lst[y])
        r1, r2 = x, y

while start < end:
    if lst[start] + lst[end] <= 0:
        find_min(start, end)
        start += 1
    
    else:
        find_min(start, end)
        end -= 1
        

print(lst[r1], lst[r2])

