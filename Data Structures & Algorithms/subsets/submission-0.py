class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol, res = [], []
        n = len(nums)
        
        def backtrack(i):
            if i == n:
                sol.append(res[:])
                return

            #Not picking the number
            backtrack(i+1)

            #Picking the number
            res.append(nums[i])                
            backtrack(i+1)
            res.pop()
                
        backtrack(0)
        return sol