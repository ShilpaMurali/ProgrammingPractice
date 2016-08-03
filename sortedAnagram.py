def sortedAnagrams(arr):
    dictAnagrams={}
    for i in range(len(arr)):
        str=sorted(arr[i])
        str=''.join(str)
        if(str in dictAnagrams):
            dictAnagrams[str].append(arr[i])
        else:
            a=[]
            a.append(arr[i])
            dictAnagrams[str]=a
    print(dictAnagrams)
    j=0
    for k,v in dictAnagrams.items():
        for i in range(len(v)):
            arr[j]=v[i]
            j+=1
    print("output is ")
    print(arr)

arr=["cat","tac","atc","zip","zap","yellow","piz","bac"]
sortedAnagrams(arr)