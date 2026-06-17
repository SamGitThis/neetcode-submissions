class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, sol = [], []
        n = len(candidates)
        curs, i = 0, 0

        def backtrack(curs, i):
            if curs == target:
                sol.append(res[:])
                return
            
            if curs > target or i == n:
                return

            res.append(candidates[i])
            backtrack(curs + candidates[i], i+1)
            res.pop()
            while i+1 < n and candidates[i] == candidates[i+1]: i+=1
            
            backtrack(curs, i+1)
        backtrack(curs,0)
        return sol