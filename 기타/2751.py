import sys
i = int(input())
for j in sorted([int(input()) for _ in range(i)]):
    sys.stdout.write(str(j)+"\n")
