class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        window_size = 0
        sett = set()
        msize = 0

        for r in range(len(s)):
            
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            window_size = (r-l) + 1
            msize = max(window_size, msize)
            sett.add(s[r])
            
        return msize