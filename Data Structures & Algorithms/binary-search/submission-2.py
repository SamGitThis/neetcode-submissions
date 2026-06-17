class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def test(index):
            if nums[index] == target:
                return True
            
            elif nums[index] > target:
                return 'l'

            else:
                return 'r'

        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l+h) // 2
            t = test(mid)

            if t is True:
                return mid
            elif t == 'l':
                h = mid - 1
            else:
                l = mid + 1
        
        return -1