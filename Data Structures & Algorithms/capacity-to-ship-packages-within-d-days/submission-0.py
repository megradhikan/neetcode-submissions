class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=sum(weights)
        l=max(weights)
        res=r

        def canship(cap):
            ships=1
            curr=cap
            for w in weights:
                if curr-w<0:
                    ships+=1
                    if ships>days:
                        return False
                    curr=cap
                curr-=w
            return True
        
        while l<=r:
            cap=(l+r)//2
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
