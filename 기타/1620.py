import sys
num, prob = map(int, input().split())
dec = {}
for i in range(num):
    dec[sys.stdin.readline().replace("\n","")] = i+1;
dec2 = {v:k for k, v in dec.items()}

for i in range (prob):
    n = sys.stdin.readline().replace("\n","")
    if (n.isdigit()):
        print(dec2[int(n)])
        
    else:
        print(dec[n])
