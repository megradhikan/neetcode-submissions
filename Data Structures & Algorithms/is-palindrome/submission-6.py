class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if len(s)==1:
            return True
        news=""
        for c in s:
            if c.isalnum():
                news+=c
        if len(news)==0:
            return True
        beg=0
        end=len(news)-1
        while beg<=len(news)//2:
            if news[beg]!=news[end]:
                return False
            beg+=1
            end-=1
        return True