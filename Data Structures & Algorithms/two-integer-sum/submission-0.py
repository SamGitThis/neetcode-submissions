class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i = {}

        for i in range(len(nums)):
            key = nums[i]
            num_i[key] = i

        for i in range (len(nums)):
            rem_add = target - nums[i]
            if rem_add in num_i and num_i[rem_add] != i:
                return [i,num_i[rem_add]]