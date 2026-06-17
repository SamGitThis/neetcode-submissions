class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxc = 0
        l, r = 0, len(heights) - 1
        
        while r > l:
            prod = (min(heights[l], heights[r])) * (r-l)
            maxc = max(maxc, prod)
            
            if heights[r] > heights[l]:
                l += 1
                
            elif heights[r] <= heights[l]:
                r -= 1
                
        return maxc