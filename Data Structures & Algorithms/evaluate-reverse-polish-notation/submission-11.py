class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenss = deque(tokens)
        stack = []
        symbols = {'+' : 0, '-' : 1, '/' : 2, '*' : 3}
         
        for i in tokenss:
            if i not in symbols:
                stack.append(i)

            elif symbols[i] == 0:
                n1, n2 = int(stack.pop()), int(stack.pop())
                stack.append(n1 + n2)

            elif symbols[i] == 1:
                n1, n2 = int(stack.pop()), int(stack.pop())
                stack.append(n2 - n1)

            elif symbols[i] == 2:
                n1, n2 = int(stack.pop()), int(stack.pop())
                stack.append(n2 / n1)

            elif symbols[i] == 3:
                n1, n2 = int(stack.pop()), int(stack.pop())
                stack.append(n2 * n1)

        print(int(stack[-1]))
        return int(stack[-1])