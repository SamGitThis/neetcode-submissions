class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mt = {
            "+" : 1,
            "-" : 2,
            "*" : 3,
            "/" : 4
        }

        stack = []

        for tk in tokens:
            if tk not in mt:
                num = int(tk)
                stack.append(num)

            else:
                sign = mt[tk]
                n2 = stack.pop()
                n1 = stack.pop()

                if sign == 1:
                    stack.append(n1+n2)
                elif sign == 2:
                    stack.append(n1-n2)
                elif sign == 3:
                    stack.append(n1*n2)
                else:
                    stack.append(int(n1/n2))

        return stack[-1]