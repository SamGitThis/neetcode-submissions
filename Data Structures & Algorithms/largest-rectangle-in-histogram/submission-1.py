class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                inde = stack.pop()
                right[inde] = i
            
            stack.append(i)

        stack = []
        left = [-1] * len(heights)

        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                inde = stack.pop()
                left[inde] = i

            stack.append(i)

        m = 0
        for i in range(len(left)):
            m = max(m, ((right[i] - left[i] - 1) * heights[i]))

        return m