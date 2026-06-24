class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        opt=[0]*n
        opt[0]=nums[0]
        opt[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            opt[i]=max(opt[i-1],opt[i-2]+nums[i])
        opt2=[0]*n
        opt2[1]=nums[1]
        if n==2:
            return max(opt[-1],opt2[-1])
        opt2[2]=max(nums[1],nums[2])
        for i in range(3,n):
            opt2[i]=max(opt2[i-1],opt2[i-2]+nums[i])
        return max(opt[-2],opt2[-1])