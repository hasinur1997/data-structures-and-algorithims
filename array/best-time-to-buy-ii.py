def best_buy_ii(prices):
    l = 0
    r = 1
    n = len(prices)
    total_profit = 0

    while r < n:
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            total_profit += profit

        l = r
        r += 1

    return total_profit


prices = [1,2,3,4,5]

print(best_buy_ii(prices))

