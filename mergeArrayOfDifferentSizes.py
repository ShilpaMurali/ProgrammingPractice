def moveToEnd(b):
    i=j=len(b)-1
    while(i>=0):
        if(b[i]!=-1):
            b[j]=b[i]
            j-=1
        i-=1
    print(b)
    return j+1
def mergeArr(s,b,bai):
    i=0
    j=0
    while(i<len(s)):
        if(bai<=len(b)-1):
            if(s[i]>b[bai]):
                b[j]=b[bai]
                bai+=1
            else:
                b[j]=s[i]
                i+=1
            print(b)
            j+=1
        else:
            break
    for k in range(i,len(s)):
        b[j]=s[k]
        j+=1
    print(b)

s=[5,8,12,14]
b=[2,-1,7,-1,-1,10,-1]
bai=moveToEnd(b)
#print(bai)
mergeArr(s,b,bai)





