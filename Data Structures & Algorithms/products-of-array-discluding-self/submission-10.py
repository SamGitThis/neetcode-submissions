class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bef, aft = [1] * len(nums), [1] * len(nums)
        res = []

        for i in range(-1, (-1 * len(nums)) -1, -1):
            if i == -1:
                continue
            else:
                aft[i] = aft[i+1] * nums[i+1]

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                bef[i] = bef[i-1] * nums[i-1]

        for i in range(len(nums)):
            res.append(bef[i] * aft[i])

        return res