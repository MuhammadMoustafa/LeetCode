class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = inf
        
        for price in prices:
            
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price-minPrice)
            
        return maxProfit
            