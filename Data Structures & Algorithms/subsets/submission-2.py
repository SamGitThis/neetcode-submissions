class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, res = [], []

        def backtrack(i):
            if i == n:
                sol.append(res[:])
                return

            backtrack(i+1)

            res.append(nums[i])
            backtrack(i+1)
            res.pop()

        backtrack(0)
        return sol