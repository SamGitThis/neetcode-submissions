class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26
        l=0
        windows = 0
        m = 0

        for r in range(len(s)):
            count[ord(s[r])-65] += 1
            windows = (r-l)+1

            while (windows-max(count)) > k:
                count[ord(s[l])-65] -= 1
                l += 1
                windows -= 1

            m = max(m, windows)
        
        return m