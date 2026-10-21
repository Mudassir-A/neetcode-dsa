class Solution:
    def reverseString(self, s):
        newStr = ""
        for ch in s:
            if ch.isalnum():
                newStr += ch.lower()

        return newStr == newStr[::-1]

    def twoPointers(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
        # return self.reverseString(s)
        return self.twoPointers(s)
