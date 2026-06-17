class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        after = [1] * len(nums)
        ans = [1] * len(nums)
        i1 = 0

        while (i1 < len(nums)):
            if i1 == 0:
                before.append(1)

            elif i1 == 1:
                before.append(nums[i1-1])

            else:
                n1 = nums[i1-1] * before[i1-1]
                before.append(n1)

            i1+= 1

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) -1:
                after[i] = 1
                ans[i] = after[i] * before[i]

            else:
                after[i] = nums[i+1] * after[i+1]
                ans[i] = after[i] * before[i]

        print(before, after)
        return ans