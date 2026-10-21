import math


class Solution:
    def bruteforce(self, tokens: List[str]) -> int:
        def isOp(ch):
            return ch in "+-*/"

        op = ""
        stack = []
        for c in tokens:
            if isOp(c):
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

        return stack[-1]

    def optimal(self, tokens):
        def dfs():
            token = tokens.pop()
            if token not in "+-/*":
                return int(token)

            right = dfs()
            left = dfs()

            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "*":
                return left * right
            elif token == "/":
                return int(left / right)

        return dfs()

    def evalRPN(self, tokens: List[str]) -> int:
        # return self.bruteforce(tokens)
        return self.optimal(tokens)
