class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target != nums[0]:
                return -1
            return 0

        if nums[0] < nums[-1]:
            minimum = 0

        else:

            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left+right) // 2

                if nums[mid] < nums[mid-1]:
                    minimum = mid
                    break
                
                elif nums[mid] < nums[right]:
                    right = mid - 1

                else:
                    left = mid + 1
        
        def bs(l, r):
            while (l <= r):
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    r = mid - 1

                else:
                    l = mid + 1

            return -1

        res = bs(0, minimum-1)
        if res != -1:
            return res

        return bs(minimum, len(nums) - 1)