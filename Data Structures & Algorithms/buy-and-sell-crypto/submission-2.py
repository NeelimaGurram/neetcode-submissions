class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        n=len(prices)
        for i in range(n):
            l=i
            r=i+1
            while l<r and r<n:
                brought_price=prices[l]
                sell_price=prices[r]
                profit=sell_price-brought_price
                max_profit=max(max_profit,profit)
                if brought_price>sell_price:
                    l+=1
                else:
                    r+=1
        return max_profit

        