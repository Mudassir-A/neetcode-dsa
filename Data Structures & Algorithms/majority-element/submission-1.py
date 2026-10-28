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

        def sorting(nums):
            nums.sort()
            return nums[len(nums) // 2]

        def bitman(nums):
            n = len(nums)
            bit = [0] * 32

            for num in nums:
                for i in range(32):
                    bit[i] += ((num >> i) & 1)
            
            res = 0

            for i in range(32):
                if bit[i] > (n // 2):
                    if i == 31:
                        res -= (1 << i)
                    else:
                        res |= (1 << i)
            return res

        # return hashmap(nums)
        # return sorting(nums)
        return bitman(nums)