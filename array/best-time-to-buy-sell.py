class Solution:
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit
            
        return maxProfit
    
# Example usage:
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
# Output: 5