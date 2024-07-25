class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        resultant=[]
        for i in range(0,len(candies)):
            if max_candies<=(candies[i]+extraCandies):
                resultant.append(True)
            else:
                resultant.append(False)
        return resultant