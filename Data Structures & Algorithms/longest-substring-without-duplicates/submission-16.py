class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
            
        l, r = 0, 1
        visited = set()
        visited.add(s[l])
        windows, ans = 0, 0

        while r < len(s):
            while r < len(s) and s[r] not in visited:
                visited.add(s[r])
                windows = (r-l) + 1
                r += 1
            
            while r < len(s) and s[r] in visited:
                visited.remove(s[l])
                l += 1
            
            ans = max(windows, ans)

        return ans