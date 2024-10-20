def myAtoi(s):
    def myAtoi(self, s: str) -> int:
        num=0
        flag=1
        taken=0
        if len(s)==0:
            return 0
        if s[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 0
        if s[0] =='-':
            flag=-1
        for i in range(0,len(s)):
            if s[i] in '0123456789':
                taken=1
                num=num*10+int(s[i])
            elif s[i]== ' ' or s[i]=='+':
                if taken==1:
                    break
                if s[i]=='+':
                    taken=1
                pass
            elif s[i]=='-' and num==0:
                if taken==1:
                    break
                taken=1
                flag=-1
            else:
                break
        num=flag*num
        if num<(-2**31):
            num=-2147483648
        elif num>(2**31 -1):
            num=2147483647
        return (num)


print(myAtoi("-91283472332"))