class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        minh = self.minheap
        maxh = self.maxheap
        heapq.heappush(minh, num)

        if abs(len(minh) - len(maxh)) > 1:
            pop_element = heapq.heappop(minh)
            heapq.heappush(maxh, -1*pop_element)

        if len(maxh) > 0 and len(minh) and (-1*maxh[0]) > minh[0]:
            x = -1 * heapq.heappop(maxh)
            y = heapq.heappop(minh)

            heapq.heappush(minh, x)
            heapq.heappush(maxh, -1*y)


        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return ((self.minheap[0] + (-1*self.maxheap[0])) / 2)
        
        else:
            return self.minheap[0]
        
        