class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                brought_price=prices[i]
                sell_price=prices[j]
                if sell_price>brought_price:
                    profit=sell_price-brought_price
                    max_profit=max(max_profit,profit)
        return max_profit

        