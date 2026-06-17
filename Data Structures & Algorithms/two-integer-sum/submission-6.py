class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indi = {}
        
        #Creating indices for every number in the list
        for i in range(len(nums)):
            num_indi[nums[i]] = i

        for i in range(len(nums)):
            tg = target - nums[i]
            
            if tg in num_indi and i != num_indi[tg]:
                return [i, num_indi[tg]]