class Solution:
    def isValid(self, s: str) -> bool:
        open={'(':')','{':'}','[':']'}
        st=[]
        for c in s:
            if c in open:
                st.append(c)
            else:
                if st:
                    ch=st.pop()
                    if c!=open[ch]:
                        return False
                else:
                    return False
        if len(st)==0:
            return True
        return False
