class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        def cond(mid, target):
            if nums[mid] == target:
                return 'f'

            elif nums[mid] > target:
                return 'l'
            
            else:
                return 'r'
        
        while(low <= high):
            mid = (low+high) // 2
            result = cond(mid, target)

            if result == 'f':
                return mid
            
            elif result == 'l':
                high = mid - 1

            else:
                low = mid + 1

        return -1