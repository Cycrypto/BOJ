def maxProfit(N, stockPrices):
    # Initialize the maximum profit to be 0
    max_profit = 0
    min_price = stockPrices[0]
    for i in range(N):
        min_price = min(min_price, stockPrices[i])
        profit = stockPrices[i] - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit

print(maxProfit(int(input()), list(map(int, input().split()))))
