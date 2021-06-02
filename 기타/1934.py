from math import gcd
for i in range (int(input())):
	x = list(map(int,input().split()))
	print((lambda x,y: x*y//gcd(x,y))(x[0],x[1]))
