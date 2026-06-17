class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxl = []
        l = 0
        m = 0

        for r in range(k):
            m = max(m, nums[r])
        
        maxl.append(m)
        m = float('-inf')
        l += 1
        r += 1

        while r < len(nums):
            m = max(nums[l:r + 1])
            maxl.append(m)
            m = float('-inf')
            l += 1
            r += 1

        return maxl