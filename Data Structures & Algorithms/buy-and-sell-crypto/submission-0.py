class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        bp=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<bp:
                bp=prices[i]
            profit=max(profit,prices[i]-bp)
        if profit>=0:
            return profit
        else:
            return 0
            
