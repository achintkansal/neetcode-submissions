class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        premax = [0] * n
        sufmax = [0] * n

        for i in range(1, n):
            premax[i] = max(premax[i-1], height[i-1])
            sufmax[(n-1)-i] = max(sufmax[n-i], height[n-i])
        
        water = 0
        for i in range(n):
            water += max(min(premax[i], sufmax[i]) - height[i], 0)
        
        return water

        
        