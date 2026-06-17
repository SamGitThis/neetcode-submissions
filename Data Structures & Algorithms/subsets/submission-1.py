class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        n = len(nums)
        
        def backtrack(i):
            if i == n:
                sol.append(res[:])
                return

            #Not picking the number

            #Picking the number
            res.append(nums[i])                
            backtrack(i+1)
            res.pop()

            backtrack(i+1)
                
        backtrack(0)
        return sol