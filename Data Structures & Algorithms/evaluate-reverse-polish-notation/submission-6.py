import math

class Solution:
    def isOp(self, ch):
        if ch in "+-*/":
            return True

    def evalRPN(self, tokens: List[str]) -> int:
        op = ""
        stack = []
        for c in tokens:
            if self.isOp(c):
                op = c
                n2 = stack.pop()
                n1 = stack.pop()

                if op == "+":
                    stack.append(n1 + n2)
                elif op == "-":
                    stack.append(n1 - n2)
                elif op == "*":
                    stack.append(n1 * n2)
                elif op == "/":
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(c))

        return (stack[-1])
