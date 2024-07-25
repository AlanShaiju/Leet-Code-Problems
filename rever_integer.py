class Solution:
    def reverse(self, x: int) -> int:
        import math
        # if math.log(x,10)==31 or math.log(x,10)==-31:
        #     return 0
        if (-2**31) <= x <= ((2**31) - 1):
            temp=abs(x)
            s=0
            while temp!=0:
                s=s*10+temp%10
                temp=temp//10
            if x<0:
                s=-s
            if (-2**31) <= s <= (2**31 - 1):
                return s
            else:
                return 0
        else:
            return 0