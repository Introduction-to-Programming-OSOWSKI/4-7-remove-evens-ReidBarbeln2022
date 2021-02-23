def removeEvens(k):
    newlist = k
    numpoped = 0
    for i in range (0 , len(newlist)):
        if newlist[i - numpoped] % 2 == 0 and newlist[i - numpoped] != 0:
            newlist.pop(i - numpoped)
            numpoped = numpoped + 1
    return newlist
   
print (removeEvens([1,2,3,4,5,6,7,8,9,10]))