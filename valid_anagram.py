class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        if s==t:
            return True
        else:
            return False