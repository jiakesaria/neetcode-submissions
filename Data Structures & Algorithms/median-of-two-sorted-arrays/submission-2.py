class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m: #binary search on smaller array 
            return self.findMedianSortedArrays(nums2, nums1)

        part_len = (n + m)//2
        l = -1
        r = min(part_len, n - 1) 

        while l <= r:
            mid1 = l + (r-l)//2 #nums1 array
            mid2 = part_len - mid1 - 2 
        
            nums1_r = nums1[mid1 + 1] if mid1 + 1 < n else float("inf")
            nums2_r = nums2[mid2 + 1] if mid2 + 1 < m else float("inf")
            nums1_l = nums1[mid1] if mid1 >= 0 else float("-inf")
            nums2_l = nums2[mid2] if mid2 >= 0 else float("-inf")

            if nums1_r >= nums2_l and nums1_l <= nums2_r:
                break #get out of while loop
            elif nums1_r < nums2[mid2]:
                l = mid1 + 1
            else:
                r = mid1 - 1
        #now we have found the mid1 and mid2 where left partition ends
        if (m + n) % 2 != 0: #odd 
            return min(nums1_r, nums2_r)
        else:
            n1 = max(nums1_l, nums2_l)
            n2 = min(nums1_r, nums2_r)
            return (n1 + n2)/2
        