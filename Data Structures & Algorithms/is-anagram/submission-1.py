class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=len(s)
        if sl!=len(t):
            return False
        sdict={}
        for c in s:
            if c in sdict:
                sdict[c]+=1
            else:
                sdict[c]=1
        for c in t:
            if c not in sdict or sdict[c]==0:
                return False
            sdict[c]-=1
        return True
            
            