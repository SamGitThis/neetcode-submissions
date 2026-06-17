class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        n = len(temperatures)
        stack = []

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                val, ind = stack.pop()
                ans[ind] = i - ind
            
            stack.append([temperatures[i], i])
        
        return ans