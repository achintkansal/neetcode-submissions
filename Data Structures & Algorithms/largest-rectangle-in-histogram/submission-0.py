class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = -1
        for i in range(n):
            curr_min = heights[i]

            left = i - 1
            right = i + 1

            while left >= 0:
                if heights[left] >= curr_min:
                    left -= 1
                else:
                    break
            
            while right < n:
                if heights[right] >= curr_min:
                    right += 1
                else:
                    break
            
            left += 1
            right -= 1
            
            max_area = max(max_area, curr_min * (right - left + 1))
            print(max_area, left, right)
        return max_area
        
            
            