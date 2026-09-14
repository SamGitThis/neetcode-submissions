class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r:
            cur_h = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, cur_h)

            if heights[l] > heights[r]:
                r -= 1
            
            else:
                l += 1

        return ans