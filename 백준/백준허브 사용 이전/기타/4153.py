while (True):
    inputs = list(map(int, input().split()))
    if sum(inputs) == 0:
        break
    
    inputs = sorted(inputs)
    if (inputs[0] ** 2 + inputs[1] ** 2 == inputs[2] ** 2):
        print("right")
    else:
        print("wrong")

