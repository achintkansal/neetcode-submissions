class Solution:
    def trap(self, height: List[int]) -> int:
        ## min(max(left), max(right)) - h[i]
        left_max = 0
        right_max = 0
        i = 0
        j = len(height) - 1
        water_stored = 0
        while i < j:
            #print(i, j)
            if height[i] < height[j]:
                dom_h = left_max
                water_stored += ((dom_h - height[i]) if (dom_h - height[i]) > 0 else 0)
                #print(dom_h - height[i])
                left_max = max(left_max, height[i])
                i += 1
            else:
                dom_h = right_max
                water_stored += ((dom_h - height[j] )if (dom_h - height[j]) > 0 else 0)
                #print(dom_h - height[j])
                right_max = max(right_max, height[j])
                j -= 1
            #print(left_max, right_max)
        
        return water_stored
        