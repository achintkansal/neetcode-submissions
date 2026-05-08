from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_elements = []

        dq = deque()
        i = 0
        j = 0
        while j < len(nums):

            while (len(dq) != 0) and (nums[j] > nums[dq[-1]]):
                dq.pop()
            dq.append(j)

            if (j - i + 1) == k:
                max_elements.append(nums[dq[0]])
                if dq[0] == i:
                    dq.popleft()
                i += 1
            
            j += 1
        
        return max_elements

                
        


        