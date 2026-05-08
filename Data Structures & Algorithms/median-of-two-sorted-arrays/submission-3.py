class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = m - 1
        even_flag = False
        tot = (m + n)
        
        if tot % 2 == 0:
            even_flag = True
        
        tot = tot // 2

        while True:
            mid = left + ((right - left) // 2)
            
            rem_element_index = (tot - (mid+1)) - 1
            l1 = nums1[mid] if mid >= 0 else float('-inf')
            r1 = nums1[mid+1] if mid < (m - 1) else float('inf')
            l2 = nums2[rem_element_index] if (rem_element_index >= 0) else float('-inf')
            r2 = nums2[rem_element_index + 1] if rem_element_index < (n - 1) else float('inf')

            if (l1 <= r2) and (l2 <= r1):
                return (max(l1, l2) + min(r1, r2)) / 2 if even_flag else min(r1, r2)
            
            elif l1 > r2:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1


        