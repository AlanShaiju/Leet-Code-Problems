def reverse(x):
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
