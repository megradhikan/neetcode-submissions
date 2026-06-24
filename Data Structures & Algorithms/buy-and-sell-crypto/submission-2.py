class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        mincost=prices[0]
        for s in prices:
            prof=max(prof,s-mincost)
            mincost=min(mincost,s)
        return prof