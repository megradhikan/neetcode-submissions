class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        opt= [0] * (n + 1)
        for i in range(2,n+1):
            opt[i]=min(opt[i-1]+cost[i-1],opt[i-2]+cost[i-2])

        return opt[-1]