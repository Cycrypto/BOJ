def min_bags(n):
    min_bags = [0] * (n + 1)
    for i in range(1, n + 1):
        min_bags[i] = float('inf')
        if i >= 3:
            min_bags[i] = min(min_bags[i], min_bags[i - 3] + 1)
        if i >= 5:
            min_bags[i] = min(min_bags[i], min_bags[i - 5] + 1)
    return min_bags[n] if min_bags[n] != float('inf') else -1

print(min_bags(int(input())))