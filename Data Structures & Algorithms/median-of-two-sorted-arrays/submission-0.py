class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1=len(nums1)
        len2=len(nums2)
        merged=nums1+nums2
        merged.sort()

        totallen=len(merged)
        if totallen%2==0:
            a=merged[totallen//2-1]
            b=merged[totallen//2]
            return (a+b)/2.0
        else:
            return merged[totallen//2]