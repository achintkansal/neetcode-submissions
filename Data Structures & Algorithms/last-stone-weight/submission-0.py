import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-1 * s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)

            diff = abs(stone1 - stone2)
            if diff > 0:
                heapq.heappush(stones, -1 * diff)
        
        if len(stones) == 0:
            return 0
        
        else:
            return -1 * stones[0]
        
        

        