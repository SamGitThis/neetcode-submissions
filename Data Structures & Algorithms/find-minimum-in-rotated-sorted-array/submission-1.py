class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')
        l, h = 0, len(nums)-1

        while l <= h:
            mid = (l+h) // 2
            minimum = min(minimum, nums[mid])

            if minimum <= nums[h]:
                h = mid - 1
            
            else:
                l = mid + 1

        return minimum