class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = [0] * (len(nums) * 2)
        for i, n in enumerate(nums):
            a[i] = n
            a[i+len(nums)] =  n

        return a