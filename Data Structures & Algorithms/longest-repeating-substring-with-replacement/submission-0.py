class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        m = [0] * 26
        windows = 0
        msize = 0
        
        for r in range(len(s)):
            m[ord(s[r]) - 65] += 1
            windows = (r-l) + 1
            
            while (windows - max(m)) > k:
                m[ord(s[l]) -65] -= 1
                windows -= 1
                l += 1
                
            msize = max(msize, windows)
            
        return msize