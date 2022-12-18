def max_wins(games):
  # Create a list of all possible mappings between numbers and gestures
  mappings = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

  # Initialize the maximum number of wins to 0
  max_wins = 0

  # Iterate through all mappings
  for mapping in mappings:
    # Initialize the number of wins for the first cow to 0
    wins = 0
    # Iterate through all games
    for game in games:
      # If the gesture of the first cow beats the gesture of the second cow according to the current mapping,
      # increment the number of wins for the first cow
      if (mapping.index(game[0]) + 1) % 3 == mapping.index(game[1]):
        wins += 1
    # Update the maximum number of wins if necessary
    max_wins = max(max_wins, wins)

  # Return the maximum number of wins
  return max_wins


n = int(input())
games = []
for i in range(n):
  games.append(list(map(int, input().split())))

# Calculate the maximum number of wins for the first cow
max_wins = max_wins(games)

# Print the result
print(max_wins)
