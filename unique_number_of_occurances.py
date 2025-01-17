def uniqueOccurrences(arr):
    d={}
    for i in arr:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    print(d)
    val=list(d.values())
    if sorted(val)==sorted(list(set(d.values()))):
        return True
    else:
        return False
print(uniqueOccurrences([-17,19,-17,-17,19,2,19,-17,19,19,2,19,0,19,19]))
