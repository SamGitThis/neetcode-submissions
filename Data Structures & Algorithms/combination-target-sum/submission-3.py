class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                sol.append(res[:])
                return
            
            if i == n or cur_sum > target:
                return

            backtrack(i+1, cur_sum)

            res.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            res.pop()
        
        backtrack(0,0)
        return sol