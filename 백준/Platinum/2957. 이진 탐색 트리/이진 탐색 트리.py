import sys
input = sys.stdin.readline

def update(i):
  check[i] = 1
  while i<=M:
    fen[i] += 1
    i += i&-i

def cal(i):
  S = 0
  while i:
    S += fen[i]
    i -= i&-i
  return S

def find(x,i,c):
  s = cal(i)
  if s==x and check[i]:
    return i
  if s<x:
    return find(x,i+(1<<c),c-1)
  return find(x,i-(1<<c),c-1)

N = int(input()); M = 1<<19
fen,check,depth = [[0]*(M+1) for i in range(3)]
C = 0
for _ in range(N):
  x = int(input()); s = cal(x)
  if fen[M]==0:
    pass
  elif s==0:
    depth[x] = depth[find(1,M,18)]+1
  elif s==fen[M]:
    depth[x] = depth[find(s,M,18)]+1
  else:
    depth[x] = max(depth[find(s,M,18)],depth[find(s+1,M,18)])+1
  C += depth[x]
  update(x)
  print(C)