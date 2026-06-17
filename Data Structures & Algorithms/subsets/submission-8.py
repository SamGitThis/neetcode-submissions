class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res , sol = [], []
        i = 0
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            backtrack(i+1)

        backtrack(i)
        return res