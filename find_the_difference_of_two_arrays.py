def findDifference(nums1,nums2):
    n1={}
    for i in nums1:
        if i in n1.keys():
            n1[i]+=1
        else:
            n1[i]=1
    n2={}
    for i in nums2:
        if i in n2.keys():
            n2[i]+=1
        else:
            n2[i]=1
    ans1=[]
    ans2=[]
    for i in n1.keys():
        if i not in n2.keys():
            ans1.append(i)
    for i in n2.keys():
        if i not in n1.keys():
            ans2.append(i)
    return [ans1,ans2]


nums1=[1,2,3]
nums2=[2,4,6]
print(findDifference(nums1,nums2))