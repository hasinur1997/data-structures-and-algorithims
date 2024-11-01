def best_buy(prices):
    l = 0
    r = 1
    n = len(prices)
    max_profit = 0

    while r < n:
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        else:
            l = r
        r += 1

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(best_buy(prices))
