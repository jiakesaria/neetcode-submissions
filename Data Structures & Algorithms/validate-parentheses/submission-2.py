class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in s:
            if i == '(' or i == '[' or i =='{':
                stck.append(i)
            else: #closing brace 
                if i == '}':
                    if not stck or stck.pop() != '{':
                        return False
                elif i == ')':
                    if not stck or stck.pop() != '(':
                        return False
                elif i == ']':
                    if not stck or stck.pop() != '[':
                        return False

        if not stck:
            return True
        return False 