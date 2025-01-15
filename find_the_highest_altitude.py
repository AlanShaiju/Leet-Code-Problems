class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max=0
        prev=0
        for i in gain:
            prev=prev+i
            if max<prev:
                max=prev
        return max

