class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for i in tokens:
            if i in '+-*/':
                b = int(stck.pop())
                a = int(stck.pop())
                if i == '+':
                    val = a + b 
                elif i == '-':
                    val = a - b
                elif i == '*':
                    val = a * b
                else:
                    val = int(a/b)
                stck.append(val)
            else:
                stck.append(int(i))
        return stck[0]