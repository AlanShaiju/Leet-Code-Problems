class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''
        l=len(word1)+len(word2)
        a=0
        b=0
        i=0
        while i<l:
            if a<len(word1):
                result=result+word1[a]
                a+=1
            if b<len(word2):
                result+=word2[b]
                b+=1
            i+=1
            
        return result