class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while r > l:
            if nums[r] + nums[l] == target:
                return [l + 1, r + 1]

            elif nums[r] + nums[l] < target:
                l += 1

            else:
                r -= 1

        return []