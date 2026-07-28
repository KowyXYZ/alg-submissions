class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            print("sell: ", sell)
            print("maxP before:", maxP)

            maxP = max(maxP, sell - minBuy)

            print("maxP before afer : ", maxP, " minBuy ", minBuy)
            minBuy = min(minBuy, sell)

        return maxP
        
       
        