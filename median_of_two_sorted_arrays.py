class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        print(nums3)
        l=len(nums3)
        if(l%2==1):
            return(nums3[int(l/2)])
        else:
            return((nums3[int(l/2)-1]+nums3[int(l/2)])/2 )