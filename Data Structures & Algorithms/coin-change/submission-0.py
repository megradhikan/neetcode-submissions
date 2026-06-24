class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt=[float('inf')]*(amount+1)
        opt[0]=0
        for i in range(1 , amount+1):
            for coin in coins:
                if i - coin >= 0:
                    opt[i] = min(opt[i], 1 + opt[i - coin])
        if opt[-1]!=float('inf'):
            return opt[-1]
        else:
            return -1
