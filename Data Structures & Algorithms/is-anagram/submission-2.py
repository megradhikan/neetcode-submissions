class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen=len(s)
        tlen=len(t)
        if slen!=tlen:
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT  
        