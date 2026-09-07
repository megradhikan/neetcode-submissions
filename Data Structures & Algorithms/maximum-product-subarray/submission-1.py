class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curmin,curmax=1,1
        for num in nums:
            tmp=curmax*num
            curmax=max(num,num*curmax,num*curmin)
            curmin=min(num,tmp,num*curmin)
            res=max(res,curmax)
        return res