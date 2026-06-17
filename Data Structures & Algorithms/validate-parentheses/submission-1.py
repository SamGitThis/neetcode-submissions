from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        map = {'}' : '{', ')' : '(', ']' : '['}

        for ch in s:
            if ch in map:
                if stack and stack[-1] == map[ch]:
                    stack.pop()

                else:
                    return False
            
            else:
                stack.append(ch)

        if stack:
            return False
        else:
            return True