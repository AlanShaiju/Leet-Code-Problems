class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(str.split(s))
        l.reverse()
        r=''
        for i in l:
            r+=i
            r+=' '
        return r.rstrip()