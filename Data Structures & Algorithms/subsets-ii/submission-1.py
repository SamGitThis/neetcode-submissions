class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        nums.sort()

        def backtrack(i):
            if i == n:
                if sol[:] not in res:
                    res.append(sol[:])
                return

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            backtrack(i+1)

        backtrack(0)
        return res