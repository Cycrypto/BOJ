inputs = list(map(int, input("").split()))
print(int(min(min(inputs[0] / 2, inputs[1]), (inputs[1]+inputs[0]-inputs[2])/3)))
