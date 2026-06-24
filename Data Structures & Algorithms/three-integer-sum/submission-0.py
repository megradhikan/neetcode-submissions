class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            begind=i+1
            lastind=n-1
            while begind<lastind:
                tsum=nums[i]+nums[begind]+nums[lastind]
                if tsum>0:
                    lastind-=1
                elif tsum<0:
                    begind+=1
                else:
                    res.append([nums[i],nums[begind],nums[lastind]])
                    begind+=1
                    lastind-=1
                    while nums[begind]==nums[begind-1] and begind<lastind:
                        begind+=1
        return res