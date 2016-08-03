def longestIncreasingSubsequenceIncr(arr,start,end):
    j=start
    arrRes=[1]*len(arr)
    for i in range(start+1,end):
        while(j<i):
            if(arr[i]>arr[j]):
                val=1+arrRes[j]
                if(val>arrRes[i]):
                    arrRes[i]=val
            j+=1
    return arrRes
def longestIncreasingSubsequenceDecr(arr,start,end):
    j=start-1
    arrRes=[1]*len(arr)
    for i in range(start-2,end-1,-1):
        while(j>i):
            if(arr[i]>arr[j]):
                val=1+arrRes[j]
                if(val>arrRes[i]):
                    arrRes[i]=val
            j-=1
    return arrRes
def maxLengthBitonicSequence(arr):
    incr=longestIncreasingSubsequenceIncr(arr,0,len(arr))
    decr=longestIncreasingSubsequenceDecr(arr,len(arr),0)
    print(incr)
    print(decr)
    count=[0]*len(arr)
    maximum=0
    for i in range(len(incr)):
        count[i]=abs(incr[i]+decr[i])-1
        if(count[i]>maximum):
            maximum=count[i]
    print("The longest bitonic subsequnce is",maximum)

arr=[12, 4, 78, 90, 45, 23]
maxLengthBitonicSequence(arr)