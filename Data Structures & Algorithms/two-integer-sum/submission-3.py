class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tm = 0

        l = dict()
        for i in range (len(nums)):
            l[nums[i]] = i

        for i in range(len(nums)):
            tm = target - nums[i]
            if tm in l and l[tm] != i:
                r = l[tm]
                if r > i:
                    return [i,r]
                
                return [r, i]