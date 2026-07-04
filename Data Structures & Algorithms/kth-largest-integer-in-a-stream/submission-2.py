import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        n = len(nums)
        self.heap = []
        self.k = k
        for i in range(n):
            
            if (len(self.heap) < k):
                heapq.heappush(self.heap, nums[i])

            elif (len(self.heap) == k) and (nums[i] > self.heap[0]):
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])
        print(self.heap)

    def add(self, val: int) -> int:
        
        if (len(self.heap) < self.k):
            heapq.heappush(self.heap, val)

        elif (len(self.heap) == self.k) and (val > self.heap[0]):
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
