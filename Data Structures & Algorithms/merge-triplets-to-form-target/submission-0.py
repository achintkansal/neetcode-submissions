class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_x, max_y, max_z = -1, -1, -1
        for x,y,z in triplets:

            if (x > target[0]) or (y > target[1]) or (z > target[2]):
                continue
            
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            max_z = max(max_z, z)
        
        return [max_x, max_y, max_z] == target
            
        