class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None

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

    def insert_at_beginning(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new

    def insert_at_end(self,data):
        if self.head is None:
            l.insert_at_beginning(data)
            return
        new=Node(data)
        head=self.head
        while head.next:
            head=head.next
        head.next=new

    def insert_at_pos(self,data,pos):
        if pos==1:
            l.insert_at_beginning(data)
            return
        new=Node(data)
        c=1
        head=self.head
        while head and c<pos-1:
            head=head.next
            c+=1
        if head is None:
            print("Out of Boundary")
            return
        temp=head.next
        head.next=new
        new.next=temp
    
    def delete_at_beginning(self):
        self.head=self.head.next
    
    def delete_at_end(self):
        head=self.head
        if head is None:
            print("Linked list is Empty")
            return
        while head.next.next:
            head=head.next
        head.next=None

    def delete_at_pos(self,pos):
        if pos==1:
            l.delete_at_beginning()
            return
        c=1
        head=self.head
        while head and c<pos-1:
            c+=1
            head=head.next
        if head.next is None:
            print("Out of boundary")
            return
        head.next=head.next.next
        
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

l=sll()
arr=[5,4,3,2,1]
for i in arr[::-1]:
    l.insert_at_beginning(i)
print(l.display())

l.insert_at_end(0)
print(l.display())

l.insert_at_pos(6,7)
print(l.display())

l.delete_at_beginning()
print(l.display())

l.delete_at_end()
print(l.display())

l.delete_at_pos(5)
print(l.display())

l.sort_sll()
print(l.display())
