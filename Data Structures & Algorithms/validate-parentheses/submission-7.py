class Solution:
    def isValid(self, s: str) -> bool:
        para = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        opening = {'{', '[', '('}
        closing = {'}', ']', ')'}

        stack = []

        for brk in s:
            if brk in opening:
                stack.append(brk)
            
            elif brk in closing:
                if not stack:
                    return False
                
                elif para[stack[-1]] == brk:
                    stack.pop()
                
                else:
                    return False

        if not stack:
            return True
        
        return False