class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        d={}
        res=[]
        for i in nums:
            d[i]=1+d.get(i,0)
        buckets= [[] for _ in range(n+2)]
        for i in d:
            buckets[d[i]+1].append(i)
        count=0
        buckets.reverse()
        for i in buckets:
            for j in i:
                if count==k:
                    break
                res.append(j)
                count+=1         
        return res


