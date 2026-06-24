class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[]
        pref.append(1)
        prod=1
        for i in range(len(nums)-1):
            prod*=nums[i]
            pref.append(prod)
        print(pref)
        post=[0]*len(nums)
        post[len(nums)-1]=1
        prod=1
        for i in range(len(nums)-2,-1,-1):
            prod*=nums[i+1]
            post[i]=prod
        print(post)
        res=[]
        for i in range(len(nums)):
            res.append(pref[i]*post[i])
        return res
