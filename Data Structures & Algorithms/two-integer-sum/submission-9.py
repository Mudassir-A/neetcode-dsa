class Solution:
    def bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    # Better Approach
    def sorting(self, nums, target):
        tmp = []
        for i, n in enumerate(nums):
            tmp.append([n, i])

        tmp.sort()

        i, j = 0, len(nums) - 1

        while i < j:
            if tmp[i][0] + tmp[j][0] == target:
                return [min(tmp[i][1], tmp[j][1]), max(tmp[i][1], tmp[j][1])]
            elif tmp[i][0] + tmp[j][0] < target:
                i += 1
            else:
                j -= 1
        return []

    # More Better Approach
    def hashmap(self, nums, target):
        mp = {}
        for i, n in enumerate(nums):
            mp[n] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if x in mp.keys() and i != mp[x]:
                return [min(i, mp[x]), max(i, mp[x])]

        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.bruteforce(nums, target)
        # return self.sorting(nums, target)
        return self.hashmap(nums, target)
