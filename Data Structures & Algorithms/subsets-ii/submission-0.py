class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i == n:
                sol.append(res[:])
                return

            res.append(nums[i])
            backtrack(i+1)
            res.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return sol