class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    
    def sort_sll(self):
        def selection_sort(arr):
            if len(arr)<2:
                return arr
            n=len(arr)
            for i in range(n-1):
                min=i
                for j in range(i+1,n):
                    if arr[j]<arr[min]:
                        min=j
                arr[i],arr[min]=arr[min],arr[i]
            return arr
        arr=l.display()
        arr=selection_sort(arr)
        self.head=None
        for i in arr[::-1]:
            l.insert_at_beginning(i)
        return arr

    def display(self):
        head=self.head
        if head is None:
            print("Empty")
            return
        a=[]
        while head:
            a.append(head.data)
            head=head.next
        return a
l=sll()
arr=[5,4,3,2,1]
for i in arr[::-1]:
    l.insert_at_beginning(i)
print(l.display())
print(l.sort_sll())
