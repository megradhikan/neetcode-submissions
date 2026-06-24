class Solution:
    def decodeString(self, s: str) -> str:
        st_stack=[]
        ct_stack=[]
        curr=""
        k=0
        for c in s:
            if c.isdigit():
                k=k*10+int(c)
            elif c=='[':
                st_stack.append(curr)
                ct_stack.append(k)
                k=0
                curr=""
            elif c==']':
                t=curr
                curr=st_stack.pop()
                count=ct_stack.pop()
                curr+=t*count
            else:
                curr+=c
        return curr

