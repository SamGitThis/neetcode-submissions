class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = { ')' : '(', ']' : '[', '}' : '{'}
        
        for b in s:
            if not stack:
                if b in close:
                    return False
                else:
                    stack.append(b)

            elif b in close and stack[-1] != close[b]:
                return False
            
            elif b in close and stack[-1] == close[b]:
                stack.pop()
            
            else:
                stack.append(b)

        if not stack:
            return True
        return False