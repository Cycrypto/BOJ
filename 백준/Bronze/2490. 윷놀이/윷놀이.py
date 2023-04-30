result = ['A', 'B', 'C', 'D', 'E']
for i in range(3):
    print(result[4 - sum(map(int,input().split())) - 1])