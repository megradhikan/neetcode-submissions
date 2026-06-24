class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen=len(s)
        tlen=len(t)
        if slen!=tlen:
            return False
        ss= "".join(sorted(s))
        st="".join(sorted(t))
        return ss==st