class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        def condition(mid, target):
            if nums[mid] == target:
                return 'f'

            if nums[mid] > target:
                return 'l'

            else:
                return 'r'

        while lo <= hi:
            mid = (lo+hi) // 2
            mov = condition(mid, target)
            print(90)

            if mov == 'f':
                return mid
            
            elif mov == 'r':
                lo = mid + 1

            else:
                hi = mid - 1

        return -1