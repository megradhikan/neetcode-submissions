class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx=0
        reslen=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    reslen=r-l+1
                    residx=l
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    reslen=r-l+1
                    residx=l
                l-=1
                r+=1
        return s[residx:residx+reslen]
