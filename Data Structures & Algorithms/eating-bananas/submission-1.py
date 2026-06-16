from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def can_finish(k):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            return hours <= h

        while left < right:
            mid = (left + right) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left