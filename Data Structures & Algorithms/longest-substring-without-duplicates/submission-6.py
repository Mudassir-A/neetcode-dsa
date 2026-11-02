class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def bruteforce(s):
            res = 0
            for i in range(len(s)):
                charSet = set()
                for j in range(i, len(s)):
                    if s[j] in charSet:
                        break
                    charSet.add(s[j])
                res = max(res, len(charSet))
            return res

        def slidingWindow(s):
            charSet = set()
            l = 0
            res = 0

            for r in range(len(s)):
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
                res = max(res, len(charSet))
            return res

        # return bruteforce(s)
        return slidingWindow(s)
