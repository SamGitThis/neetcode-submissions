class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v_p = {}

        for i in range(len(nums)):
            v_p[nums[i]] = i
        
        print(v_p)

        for i in range(len(nums)):
            t = target - nums[i]
            if t in v_p and i != v_p[t]:
                return [i, v_p[t]]