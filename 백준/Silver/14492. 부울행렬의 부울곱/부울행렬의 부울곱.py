def solve(n, A, B):
  C = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] |= A[i][k] and B[k][j]


  count = 0
  for i in range(n):
    for j in range(n):
      if C[i][j] == 1:
        count += 1

  return count


n = int(input())
A =[]
B = []

for _ in range(n):
	A.append([int(x) for x in input().split()])

for _ in range(n):
	B.append([int(x) for x in input().split()])


print(solve(n, A, B))
