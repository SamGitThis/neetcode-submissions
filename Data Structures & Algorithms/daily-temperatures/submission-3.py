class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return
            
        t = temperatures
        l = len(t)
        ans = [0] * l
        stack = []

        for i in range(l):
            while stack and stack[-1][-1] < t[i]:
                inde, val = stack.pop()
                ans[inde] = i - inde
            
            stack.append([i, t[i]])

        return ans