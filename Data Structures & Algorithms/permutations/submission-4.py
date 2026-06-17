class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(res) == n:
                sol.append(res[:])
                return

            for i in nums:
                if i not in res:
                    res.append(i)
                    backtrack()
                    res.pop()

        backtrack()
        return sol