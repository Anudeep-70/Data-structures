def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return "Found at "+str(i)
    return "Not found"
def binsearch(arr):
    arr.sort()
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==mid+1:
            low=mid+1
        else:
            high=mid-1
    return low+1

arr=[1,2,3,4,5,6,8,9,10]
print(binsearch(arr))
exit()
