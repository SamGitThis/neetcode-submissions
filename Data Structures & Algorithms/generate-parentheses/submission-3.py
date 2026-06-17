class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def btrack(openn, close):
            if openn == close == n:
                res.append("".join(stack))
                return

            if openn < n:
                stack.append('(')
                btrack(openn+1, close)
                stack.pop()

            if close < openn:
                stack.append(')')
                btrack(openn, close + 1)
                stack.pop()

        btrack(0, 0)
        return res