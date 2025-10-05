def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr

def mergesort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    l,r=arr[0:mid],arr[mid:]
    l=mergesort(l)
    r=mergesort(r)
    return merge(l,r)
def merge(l,r):
    i,j=0,0
    new=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            new.append(l[i])
            i+=1
        else:
            new.append(r[j])
            j+=1
    new.extend(l[i:])
    new.extend(r[j:])
    return new

def quicksort(arr):
    if len(arr)<=1:
        return arr
    p=arr[len(arr)//2]
    left=[x for x in arr if x<p]
    right=[x for x in arr if x>p]
    middle=[x for x in arr if x==p]
    return quicksort(left)+middle+quicksort(right)

arr=[7,4,3,2,6,5,1,9,8]
print(quicksort(arr))