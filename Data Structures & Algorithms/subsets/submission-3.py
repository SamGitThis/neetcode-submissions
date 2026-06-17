class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res , ans = [], []
        i = 0
        n = len(nums)

        def backtrack(i):
            if i == n:
                ans.append(res[:])
                return
            
            backtrack(i+1)

            res.append(nums[i])
            backtrack(i+1)
            res.pop()

        backtrack(i)
        return ans