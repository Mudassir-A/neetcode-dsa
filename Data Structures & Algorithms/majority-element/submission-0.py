class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def hashmap(nums):
            mp = {}
            for n in nums:
                if n in mp:
                    mp[n] += 1
                else:
                    mp[n] = 1

            for k, v in mp.items():
                if v > len(nums) / 2:
                    return k

            return -1

        return hashmap(nums)