def maxArea(height):
        pointer_1=0
        pointer_2=len(height)-1
        length=len(height)-1
        output=0
        while pointer_1!=pointer_2:
            if min(height[pointer_1],height[pointer_2])*length>output:
                output=min(height[pointer_1],height[pointer_2])*length
            length-=1
            if height[pointer_1]<height[pointer_2]:
                pointer_1+=1
            else:
                pointer_2-=1
        return output
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))