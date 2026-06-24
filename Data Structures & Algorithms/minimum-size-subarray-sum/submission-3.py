class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        r=0
        m=float("inf")
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                        win=r-l+1
                        m=min(m,win)
                        s-=nums[l]
                        l+=1
        if m!=float("inf"):
            return m
        return 0