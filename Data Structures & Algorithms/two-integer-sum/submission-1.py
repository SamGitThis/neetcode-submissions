class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}
        for i in range(len(nums)):
            key = nums[i]
            hasht[key] = i

        for i in range(len(nums)):
            rem = target - nums[i]
            
            if rem in hasht and i != hasht[rem]:
                return [i, hasht[rem]]