import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        punc = string.punctuation
        low = 0
        new = ""

        for i in s:
            if (i not in punc) and (i != " "):
                new += i.lower()

        high = len(new) - 1

        while high > low:
            if new[high] == new[low]:
                high -= 1
                low += 1

            else:
                return False

        return True