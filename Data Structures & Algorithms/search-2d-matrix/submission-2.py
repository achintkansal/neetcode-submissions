class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # check 1st column wise

        left = 0
        right = m
        
        while left < right:
            mid = left + (right - left) // 2
            
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                right = mid
            else:
                left = mid + 1

        index_col = left - 1
        
        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if matrix[index_col][mid] == target:
                return True
            elif target > matrix[index_col][mid]:
                left = mid + 1
            else:
                right = mid
        return False
        