class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
        """
        max_profit = 0
        for i in range(len(prices)-1):
            currentProfit = max(prices[i+1:]) - prices[i]
            if currentProfit > max_profit:
                max_profit = currentProfit
        
        return max_profit
        """
            
        