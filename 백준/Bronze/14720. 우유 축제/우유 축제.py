def maximum_milk(n, stores):
  count = 0
  for store in stores:
    if store == count % 3:
      count += 1
  return count


print(maximum_milk(int(input()), list(map(int, input().split()))))