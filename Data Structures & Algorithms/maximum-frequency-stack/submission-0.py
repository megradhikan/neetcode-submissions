class FreqStack:

    def __init__(self):
        self.cnt={}
        self.maxCnt=0
        self.stacks={}

    def push(self, val: int) -> None:
        c=self.cnt.get(val,0)+1
        self.cnt[val]=c
        if c> self.maxCnt:
            self.maxCnt=c
            self.stacks[c]=[]
        self.stacks[c].append(val)

    def pop(self) -> int:
        res=self.stacks[self.maxCnt].pop()
        self.cnt[res]-=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()