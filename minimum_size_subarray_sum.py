class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=[]
        i,j=0,0
        sums=0
        while j<=len(nums):
            if sums>=target:
                l.append(j-i)
                sums=sums-nums[i]
                i+=1
            elif j<len(nums):
                sums+=nums[j]
                j+=1
            else:
                j+=1
        if len(l)==0:
            return 0
        else:
            return min(l)