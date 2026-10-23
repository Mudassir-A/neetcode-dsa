class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bruteforce(piles, h):
            speed = 1
            while True:
                totalTime = 0
                for pile in piles:
                    totalTime += math.ceil(pile / speed)
                if totalTime <= h:
                    return speed
                speed += 1
            return speed

        def binarySearch(piles, h):
            left, right = 1, max(piles)
            res = right

            while left <= right:
                mid = (left + right) // 2
                totalTime = 0
                for p in piles:
                    totalTime += math.ceil(float(p) / mid)
                if totalTime <= h:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        # return bruteforce(piles, h)
        return binarySearch(piles, h)
