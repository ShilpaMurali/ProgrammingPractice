def swap(arr,x,y):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp

def segregateOnesAndZeroes(arr):
    index=0
    for i in range(len(arr)-1):
        if(arr[i]>arr[i+1]):
            if(index):
                swap(arr,i+1,index)
                index+=1
            else:
                swap(arr,i,i+1)
        elif(arr[i]==1 and arr[i]==arr[i+1]):
            if(not index):
                index=i
    return arr


arr=[0,1,0,1,0,0,1,1,1,0]
arr=[0, 1, 0, 1, 1, 1]
print(segregateOnesAndZeroes(arr))
        