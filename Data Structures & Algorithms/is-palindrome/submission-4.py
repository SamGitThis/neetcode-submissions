import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0  or len(s) == 1:
            return True

        l = 0 
        punc = string.punctuation
        new = ""

        for i in s:
            if i not in punc and i != " ":
                new += i
        r = len(new) -1

        while r > l:
            if new[r].lower() != new[l].lower():
                return False
            
            else:
                l += 1
                r -= 1

        return True