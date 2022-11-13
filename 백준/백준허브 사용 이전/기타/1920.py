l = int(input())
list1 = list(map(int, input().split()))

l2 = int(input())
list2 = list(map(int, input().split()))
for i in list2:
    if i in list1:
        print("1")

    else:
        print("0")
    

