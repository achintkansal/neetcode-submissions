from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        i = 0
        while i < k:
            heappush(heap, (-1*nums[i], i))
            i += 1
        
        i = 0
        j = k-1
        max_window = []
        while j < len(nums):
            curr_element, curr_index = heap[0]
            if curr_index >= i and curr_index <= j:
                max_window.append(curr_element * -1)
            else:
                while curr_index < i or curr_index > j:
                    heappop(heap)
                    curr_element , curr_index = heap[0]

                max_window.append(curr_element * -1)
            
            i += 1
            j += 1
            if j < len(nums):
                heappush(heap, (-1*nums[j], j))
            
        return max_window
        


        