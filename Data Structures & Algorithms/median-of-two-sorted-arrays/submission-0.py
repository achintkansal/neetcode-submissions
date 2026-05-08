class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        ## Always nums1 <= nums2
        flag = ((n + m) % 2 == 0)
                
        left1 = 0
        right = n-1 ## because list can be empty also
        half = (n + m) // 2

        while True:
            mid1 = left1 + (right - left1) // 2
            mid2 = half - (mid1+1) - 1 ## -1 for indexing and (half - (mid1+1)) number of elements in array nums2
            
            #l1 = nums1[mid1] if mid1 >=0 else float('-inf')
            l1 = float('-inf') if mid1 < 0 else nums1[mid1]
            
            #r1 = nums1[mid1+1] if mid1 < n else float('inf')
            r1 = float('inf') if (mid1+1) >= n else nums1[mid1+1]
            

            #l2 = nums2[mid2] if mid2 >=0 else float('-inf')
            l2 = float('-inf') if mid2 < 0 else nums2[mid2]
            
            #r2 = nums2[mid2+1] if mid2 < m else float('inf')
            r2 = float('inf') if (mid2+1) >= m else nums2[mid2+1]
            
            if (l1 <= r2) and (l2 <= r1):
                if flag: ## even
                    return (max(l1, l2) + min(r1,r2)) / 2
                else: ## odd
                    return min(r1,r2)
            
            if l1 > r2:
                right = mid1 - 1
            else:
                left1 = mid1 + 1
        return -1





        