class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        opt=[0]*n
        opt[0]=nums[0]
        opt[1]=max(nums[0],nums[1])
        for i in range(2,n):
            opt[i]=max(opt[i-1],opt[i-2]+nums[i])
        return opt[-1]