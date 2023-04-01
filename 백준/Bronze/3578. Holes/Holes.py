n = int(input())
if n == 0:
  print(1)
elif n == 1:
  print(0)
else:
  if n % 2 != 0:
    print(4, end='')
  for i in range(n//2):
    print(8, end='')