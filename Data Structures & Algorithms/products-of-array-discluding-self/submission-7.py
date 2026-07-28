class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        before = []
        after = []
        
        product = 1

        for i in range(len(nums)):
            bef = i - 1
            aft = i + 1
            while bef > -1:
                product *= nums[bef]
                bef -= 1

            before.append(product)
            product = 1

            while aft < len(nums):
                product *= nums[aft]
                aft += 1
            
            after.append(product)
            product = 1

            ans.append(before[i] * after[i])

        print(before)
        print(after)

        return ans