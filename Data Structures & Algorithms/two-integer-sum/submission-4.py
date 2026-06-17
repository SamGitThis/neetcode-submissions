class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while (i < len(nums)):
            firstn = nums[i]
            for n in range(i+1, len(nums)):
                if firstn + nums[n] == target:
                    return [i, n]
            
            i += 1