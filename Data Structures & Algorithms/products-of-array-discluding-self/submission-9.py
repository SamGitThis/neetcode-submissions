class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, z = 1, 0
        res = [1] * len(nums)

        for num in nums:
            if num != 0:
                prod *= num
            else:
                z += 1

        if z > 1:
            return [0] * len(nums)

        if z == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = prod
        
        else:
            for i in range(len(nums)):
                res[i] = prod // nums[i]

        return res