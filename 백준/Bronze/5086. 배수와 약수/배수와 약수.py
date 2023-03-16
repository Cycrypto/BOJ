while((inp:= tuple(map(int, input().split()))) != (0, 0)):
  if not inp[1] % inp[0]:
    print("factor")

  elif not (inp[0] % inp[1]):
    print("multiple")

  else:
    print("neither")