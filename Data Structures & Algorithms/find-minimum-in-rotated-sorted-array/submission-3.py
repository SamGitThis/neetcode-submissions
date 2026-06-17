class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        minimum = float('inf')
        l, r = 0, len(nums) - 1

        while (l <= r):
            mid = (l+r) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] < nums[r]:
                r = mid - 1

            else:
                l = mid + 1

        return minimum