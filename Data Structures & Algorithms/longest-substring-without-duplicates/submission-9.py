class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1

        l, r = 0, 0
        visited = set()
        windowsize = 0
        mlength = 1

        while r <= len(s) - 1:
            while r < len(s) and s[r] not in visited:
                visited.add(s[r])
                r += 1

            windowsize = ((r-1)-l) + 1
            mlength = max(mlength, windowsize)
            visited.remove(s[l])
            l += 1

        return mlength