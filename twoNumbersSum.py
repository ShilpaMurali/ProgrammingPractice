def twoNumbersSum(arr):
    sortedArr=arr
    sortedArr.sort()
    print(sortedArr)
    j=len(sortedArr)-1
    i=0
    while(i!=j):
        if(sortedArr[i]+sortedArr[j]==0):
            print(sortedArr[i],sortedArr[j])
            j-=1
        else:
            i+=1

def threeNumbersSum(arr):
    sortedArr=arr
    sortedArr.sort()
    print(sortedArr)
    j=len(sortedArr)-1
    i=0
    k=j-1
    while(i<j):
        currSum=sortedArr[i]+sortedArr[j]
        while(k>i):
            if(currSum+sortedArr[k]==0):
                print(sortedArr[i],sortedArr[j],sortedArr[k]) 
            k-=1
        j-=1
        k=j-1
        if(j==i):
            i+=1
            j=len(sortedArr)-1
        else:
            i-=1
arr=[2,3,1,-2,-1,0,2,-3,0]
twoNumbersSum(arr)
threeNumbersSum(arr)