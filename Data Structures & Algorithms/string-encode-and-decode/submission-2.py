class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            wordlen=int(s[i:j])
            word=s[j+1:j+1+wordlen]
            decoded.append(word)
            i=j+wordlen+1
        return decoded

