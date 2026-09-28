class Solution:
    def bruteforce(self, nums):
        """Time limit exceeds"""
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res

    def division(self, nums):
        prod, zero_cnt = 1, 0
        for n in nums:
            if n:
                prod *= n
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res

    def prefixSuffix(self, nums):
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return self.bruteforce(nums)
        # return self.division(nums)
        return self.prefixSuffix(nums)
