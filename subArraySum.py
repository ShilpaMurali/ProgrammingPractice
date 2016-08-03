def subArraySum(arr,sum):
    sumVal=arr[0]
    j=0
    for i in range(1,len(arr)):
        sumVal+=arr[i]
        if(sumVal>sum):
            while(sumVal>sum):
                sumVal-=arr[j]
                j+=1
        if(sumVal==sum):
            print(j,i)
            break;
    if(sumVal!=sum):
        print("None")
                
arr=[1, 4]
sum=7
subArraySum(arr, sum)