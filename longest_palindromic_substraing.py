class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings=[]
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                substrings.append(s[i:j])
        substrings=sorted(substrings,key=len,reverse=True)
        for x in substrings:
            if x==x[::-1]:
                return x