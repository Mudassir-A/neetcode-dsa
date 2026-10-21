class Solution:
    def bruteforce(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > t:
                    res[i] = j - i
                    break
                else:
                    j += 1
        return res

    def usingStack(self, temperatures):
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return self.bruteforce(temperatures)
        return self.usingStack(temperatures)
