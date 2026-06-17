class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(close, openn):
            if close == openn == n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append('(')
                backtrack(close, openn + 1)
                stack.pop()

            if close < openn:
                stack.append(')')
                backtrack(close+1, openn)
                stack.pop()

        backtrack(0,0)
        return res