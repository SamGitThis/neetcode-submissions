class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def test_loc(mid):

            print(nums[mid])
            if nums[mid] == target:
                return 'found'

            elif nums[mid] < target:
                return 'right'

            else:
                return 'left'

        lowend, highend = 0, len(nums) - 1
        
        while lowend <= highend:
            mid = (lowend + highend) // 2
            result = test_loc(mid)

            if result == 'found':
                return mid
            
            elif result == 'right':
                lowend = mid + 1

            elif result == 'left':
                highend = mid - 1

        return -1