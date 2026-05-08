import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        left = 1
        right = max_pile
        k = -1
        while left <= right:
            mid = left + (right - left) // 2
            hrs_to_eat = 0
            for p in piles:
                hrs_to_eat += math.ceil(p/mid)
            if hrs_to_eat > h:
                left = mid + 1
            else:
                k = mid
                right = mid - 1

        return k
            
        