class Solution:
    def reverseVowels(self, s: str) -> str:
        result=[]
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in vowels:
                result.append(i)
        i=len(result)-1
        r=''
        for j in range(0,len(s)):
            if s[j] in vowels:
                r+=result[i]
                i-=1
            else:
                r+=s[j]
        return r