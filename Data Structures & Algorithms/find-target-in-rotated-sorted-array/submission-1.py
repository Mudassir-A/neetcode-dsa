class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bruteforce(nums, target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1

        def pivotal(nums, target):
            low, right = 0, len(nums) - 1

            while low < right:
                mid = low + (right - low) // 2

                if nums[mid] > nums[right]:
                    low = mid + 1
                else:
                    right = mid

            pivot = low

            def binarySearch(low, high):
                while low <= high:
                    mid = (low + high) // 2

                    if nums[mid] < target:
                        low += 1
                    elif nums[mid] > target:
                        high -= 1
                    else:
                        return mid
                return -1

            result = binarySearch(0, pivot - 1)

            if result != -1:
                return result

            return binarySearch(pivot, len(nums) - 1)

        # return bruteforce(nums, target)
        return pivotal(nums, target)
