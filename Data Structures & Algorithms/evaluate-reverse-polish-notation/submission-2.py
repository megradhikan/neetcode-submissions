class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands=[]
        operators=set(['+','-','*','/'])
        for i in tokens:
            if i not in operators:
                operands.append(int(i))
            else:
                op1=operands.pop()
                op2=operands.pop()
                if i=='+':
                    ans=op1+op2
                elif i=='-':
                    ans=op2-op1
                elif i=='*':
                    ans=op1*op2
                else:
                    ans=int(float(op2)/op1)
                operands.append(ans)
        return operands[-1]
