class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        visited = set()
        windowsize = 0
        mlength = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            windowsize = (r-l) + 1
            mlength = max(mlength, windowsize)
            visited.add(s[r])

        return mlength